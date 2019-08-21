import pandas as pd
"""
Class Breaker
    Breaks a session into Request and Response pieces,
    A request followed by a response from now one will be called an 'act'. 
    act: like a part of a play, or 'מערכה' in hebrew
"""


class Breaker(object):
    def __init__(self, delta_t=0.03, threshold_t=300):
        """threshold_t, represents GET minimum request size"""
        self.threshold_t = threshold_t
        """delta_t, minimum time between requests"""
        self.delta_t = delta_t

    """returns pandas dataframe[], with each element being a request and its response"""
    def sess_break(self, df):
        acts = []
        request_start_time = 0
        act = []

        for index, row in df.iterrows():
            """check for clients packets requests"""
            if 'UDP' in row['key']:
                dst_port = row['udp.dstport']
            else:
                dst_port = row['tcp.dstport']

            if dst_port == 443 and row['frame.len'] > self.threshold_t and\
                    (request_start_time == 0 or ((row['frame.time_epoch'] - request_start_time) > self.delta_t)):
                if act:
                    acts.append(pd.DataFrame(df.loc[act]))
                    act.clear()

                request_start_time = row['frame.time_epoch']
                act.append(index)

            else:
                if act:
                    act.append(index)

        if act:
            acts.append(pd.DataFrame(df.loc[act]))
        if not acts:
            print(df[['key','frame.len']])
        return acts

    """returns list of data frames, each data frame is an act"""
    def get_dfs(self, df):
        return self.sess_break(df)

    def get_bins(self, bin_size=3, df=None, df_list=None):
        if df_list is None:
            acts = self.sess_break(df)
        else:
            acts = df_list
        bins_list = []
        df = []
        if len(acts) < bin_size:
            bins_list.append(acts)
            return bins_list
        for i in range(len(acts) - bin_size + 1):
            for j in range(bin_size):
                df.append(acts[i + j])
            bins_list.append(df)
            df = []
        return bins_list


