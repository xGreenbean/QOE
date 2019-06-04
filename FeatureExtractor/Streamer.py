from containers.PacketContainer import PacketContainer
from containers.Session import Session

import datetime
import pandas as pd
"""
Class Streamer
    holds an interaction, built for functions 'get_video_related_sessions'
    which returns the video_related_sessions in the Interaction.
    delta_t = time between connection opening time
    delta_s = time to split sessions by
    threshold_p = payload threshold, if time interval t for sessions s surpasses it,
    it is considered a video session
"""


class Streamer(PacketContainer):
    def __init__(self, interaction, delta_s, delta_t, threshold_p):
        super(Streamer, self).__init__(interaction.pcap_df)
        self.interaction = interaction
        self.delta_s = delta_s
        self.delta_t = delta_t
        self.threshold_p = threshold_p
        self.all_sessions = list(self.interaction.get_sessions())
        self.video_related_sessions = []
        self.not_video_related_sessions = []
    """returns the video_related streams
    This function is threshold based, if a sessions surpasses the threshold,
    it is considered video and all sessions to same Server, and sessions with 
    'close' opening times are added to the list."""

    def get_video_related_sessions(self):
        #prepare sessions time_groups
        time_groups = []
        df = self.interaction.getSample()
        df['date'] = df['frame.time_epoch'].\
            apply(datetime.datetime.fromtimestamp)  # convert epoch to datetime.

        group_intervals = df.groupby(pd.Grouper(key='date', freq=(str(self.delta_s) + 'S')))

        sess_payload_dict = {}  # dict hold for each session its current payload aggregation.

        for item in group_intervals:
            time_groups.append(item[1])  # item[1] contains the dataframe

        for time_group in time_groups:
            for index, row in time_group.iterrows():  # aggregate payloads for sessions in time group.
                key = self.get_session_string(row)  # we need a key for the dictionary

                if key in sess_payload_dict:
                    sess_payload_dict[key] += row['frame.len']

                else:
                    sess_payload_dict[key] = 0
                    sess_payload_dict[key] += row['frame.len']

            for sess_key, payload in sess_payload_dict.items():  # check for payload surpassing threshold

                if payload > self.threshold_p:
                    video_sess = self.interaction.get_session(sess_key)  # get session object from key

                    if video_sess not in self.video_related_sessions:
                        print('passsed threshold', video_sess.to_filter())
                        self.video_related_sessions.append(video_sess)
                        self.add_server_related_sessions(video_sess)
                        self.add_time_related_sessions(video_sess)

            sess_payload_dict.clear()
        return self.video_related_sessions


    def get_not_video_related_sessions(self):
        if len(self.video_related_sessions) == 0:
            self.get_video_related_sessions()
        for sess in self.interaction.get_sessions():
            if sess not in self.video_related_sessions:
                self.not_video_related_sessions.append(sess)
        return self.not_video_related_sessions

    """ add sessions to video_related_sessions by server where dstport is 443"""
    def add_server_related_sessions(self, video_session):
        for sess in self.all_sessions:
            if sess.srcIp == video_session.srcIp and sess.dstIp == video_session.dstIp and \
                    sess.dstPort == 443:
                if sess not in self.video_related_sessions:
                    print('same server', sess.to_filter())
                    self.video_related_sessions.append(sess)

    """ add sessions to video_related_sessions by server where opening_time is close"""
    def add_time_related_sessions(self, video_session):
        for sess in self.all_sessions:
            if abs(sess.connection_opening_time - video_session.connection_opening_time) < self.delta_t:
                if sess not in self.video_related_sessions:
                    print('close connection time', sess.to_filter())
                    self.video_related_sessions.append(sess)

    def getSample(self):
        return self.video_related_sessions

    """
    input: data frame row
    output: a string representing the row. ie port's and ip's.
    """
    def get_session_string(self, row):
        if row['ip.src'] == self.interaction.get_client_ip():
            if row['tcp.srcport'] > 0:
                curr_fiveple = ['TCP', row['tcp.srcport'], row['tcp.dstport'], row['ip.src'], row['ip.dst']]
            else:
                curr_fiveple = ['UDP', row['udp.srcport'], row['udp.dstport'], row['ip.src'], row['ip.dst']]

        elif row['tcp.srcport'] > 0:
            curr_fiveple = ['TCP', row['tcp.dstport'], row['tcp.srcport'], row['ip.dst'], row['ip.src']]
        else:
            curr_fiveple = ['UDP', row['udp.dstport'], row['udp.srcport'], row['ip.dst'],  row['ip.src']]

        return ''.join(str(x) + ' ' for x in curr_fiveple)
