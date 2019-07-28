from tools.Breaker import Breaker
from containers.Interaction import Interaction
import pandas as pd
import datetime

global up_link
global down_link
global num_req_res
global first_packet_time
global last_packet_time

up_link = 0
down_link = 1
num_req_res = 2
first_packet_time = 3
last_packet_time = 4


class BigPacket:

    def __init__(self, interval_size, csv_path, lookup_sni):
        self.interval_size = interval_size
        self.df = pd.read_csv(csv_path)
        self.sni = lookup_sni

    def bp_break(self):
        df_list = self.calculate_sessions_intervals()
        aggregation_list = BigPacket.aggregate_session_intervals(df_list)
        selected_intervals = []
        curr_interval = []
        for i in range(len(aggregation_list)):
            if curr_interval and aggregation_list[i][num_req_res] > 0:
                selected_intervals.append(curr_interval)
                curr_interval = aggregation_list[i]
            else:
                if i != 0:
                    curr_interval[up_link] += aggregation_list[i][up_link]
                    curr_interval[down_link] += aggregation_list[i][down_link]
                    curr_interval[num_req_res] += aggregation_list[i][num_req_res]
                    curr_interval[first_packet_time] = min(aggregation_list[i][first_packet_time],
                                                           curr_interval[first_packet_time])
                    curr_interval[last_packet_time] = max(aggregation_list[i][last_packet_time],
                                                          curr_interval[last_packet_time])
                else:
                    curr_interval = aggregation_list[i]

            if i == len(aggregation_list) - 1:
                selected_intervals.append(curr_interval)
        return selected_intervals

    def divide_intervals(self):
        df = self.df.dropna(subset=['frame.time_epoch'])
        df['date'] = df['frame.time_epoch'].apply(datetime.datetime.fromtimestamp)
        group_intervals = df.groupby(pd.Grouper(key='date', freq=(str(self.interval_size) + 'S')))
        return group_intervals

    def calculate_sessions_intervals(self):
        df_list = []
        sni_dic = {}
        divided_intervals = self.divide_intervals()
        for item in divided_intervals:
            temp_interaction = Interaction(item[1])
            dict_sess = {}
            for sess in temp_interaction.get_sessions():
                if sess.get_sni() is not "None":
                    sess_sni = sess.get_sni()
                    sni_dic[sess.get_string()] = sess.get_sni()
                else:
                    sess_sni = sni_dic[sess.get_string()]

                if self.sni in sess_sni:
                    req_res_list = Breaker(sess)
                    flow_up, flow_down = sess.get_flows()
                    up_link_size = flow_up['frame.len'].sum()
                    down_link_size = flow_down['frame.len'].sum()
                    dict_sess[sess.get_string()] = [up_link_size,
                                                    down_link_size, len(req_res_list.get_dfs()),
                                                    sess.get_df()['frame.time_epoch'].iloc[0],
                                                    sess.get_df()['frame.time_epoch'].iloc[len(sess.get_df()) - 1]]
            if len(dict_sess) != 0:
                df_list.append(dict_sess)
        return df_list

    @staticmethod
    def aggregate_session_intervals(interval_list):
        aggregation_list = []
        for curr_dict in interval_list:
            start_epoch_list = []
            end_epoch_list = []
            up_link_sum = 0
            down_link_sum = 0
            req_res_counter = 0
            for key in curr_dict:
                up_link_sum += curr_dict[key][0]
                down_link_sum += curr_dict[key][1]
                req_res_counter += curr_dict[key][2]
                start_epoch_list.append(curr_dict[key][3])
                end_epoch_list.append(curr_dict[key][4])
            aggregation_list.append([up_link_sum, down_link_sum, req_res_counter, min(start_epoch_list),
                                     max(end_epoch_list)])
        return aggregation_list