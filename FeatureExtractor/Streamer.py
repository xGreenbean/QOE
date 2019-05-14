from containers.Interaction import *
"""
Class Streamer
    holds an interaction, build for functions 'get_video_related_sessions'
    which returns the video_related_sessions in the Interaction.
    delta_t = time between connection opening time
    delta_s = time to split sessions by
    threshold_p = payload threshold, if time interval t for sessions s surpasses it,
    it is considered a video session
"""


class Streamer:
    def __init__(self, interaction, delta_s, delta_t, threshold_p):
        self.interaction = interaction
        self.video_related_sessions = []
        self.delta_s = delta_s
        self.delta_t = delta_t
        self.threshold_p = threshold_p
        self.all_sessions = list(self.interaction.get_sessions())
        self.video_related_sessions = []

    """returns the video_related streams
    This function is threshold based, if a sessions surpasses the threshold,
    it is considered video and all sessions to same Server, and sessions with 
    'close' opening times are added to the list."""
    def get_video_related_sessions(self):
        if len(self.video_related_sessions) == 0:
            start_time = self.interaction.pcap_df['frame.time_epoch'].min()
            end_time = self.interaction.pcap_df['frame.time_epoch'].max()
            time_interval = end_time - start_time
            payloads = 0

            for t in range(int(time_interval / self.delta_s)):
                for sess in self.all_sessions:
                    for index, row in sess.all_packets.iterrows():
                        if abs(row['frame.time_epoch'] - (start_time + t)) <= self.delta_s:
                            payloads += row['frame.len']
                        elif row['frame.time_epoch'] - (start_time + t) > self.delta_s:
                            break
                    if payloads >= self.threshold_p:
                        if sess not in self.video_related_sessions:
                            self.video_related_sessions.append(sess)
                            self.add_time_related_sessions(sess)
                            self.add_server_related_sessions(sess)
                            self.all_sessions.remove(sess)
                    payloads = 0
        return self.video_related_sessions

    """ add sessions to video_related_sessions by server where dstport is 443"""
    def add_server_related_sessions(self, video_session):
        for sess in self.all_sessions:
            if sess.srcIp == video_session.srcIp and sess.dstIp == video_session.dstIp and \
                    sess.dstPort == 443:
                if sess not in self.video_related_sessions:
                    self.video_related_sessions.append(sess)

    """ add sessions to video_related_sessions by server where opening_time is close"""
    def add_time_related_sessions(self, video_session):
        for sess in self.all_sessions:
            if abs(sess.connection_opening_time - video_session.connection_opening_time) < self.delta_t:
                if sess not in self.video_related_sessions:
                    self.video_related_sessions.append(sess)
