import pandas as pd
from containers.Session import *
from Streamer import *
"""
Class Interaction
    defines interaction between client and the internet,
    -> for our purpose it is a collection of packet containing some interaction,
    that we have recorded.
"""


class Interaction:

    def __init__(self, pcap_df):
        self.clientIP = 0
        self.pcap_df = pcap_df
        self.sessions = []

    """returns client's ip, we take the ip.src from the first packet where tcp.syn = 1 and tcp.ack = 0 """
    def get_client_ip(self):
        if self.clientIP != 0:
            return self.clientIP
        else:
            for index, row in self.pcap_df.iterrows():
                if row['tcp.flags.syn'] == 1 and row['tcp.flags.ack'] == 0:
                    self.clientIP = row['ip.src']
                    return self.clientIP

    """returns List of sessions, a session is a 4 tuple ipsrc,portsrc,ipdst,portdst"""
    ## Maybe should handle better the TCP\UDP seperation.
    def get_sessions(self):
        curr_5ple = None
        if len(self.sessions) == 0:
            sessions_list = []
            for index, row in self.pcap_df.iterrows():
                if row['udp.srcport'] > 0:
                    curr_5ple = ['UDP', row['ip.src'], row['udp.srcport'], row['ip.dst'], row['udp.dstport']]
                else:
                    curr_5ple = ['TCP', row['ip.src'], row['tcp.srcport'], row['ip.dst'], row['tcp.dstport']]
                if curr_5ple not in sessions_list and\
                        [curr_5ple[0], curr_5ple[3], curr_5ple[4], curr_5ple[1], curr_5ple[2]] not in sessions_list:
                        sessions_list.append(curr_5ple)
                        self.sessions.append(Session(curr_5ple[0], curr_5ple[2],
                                                     curr_5ple[4], curr_5ple[1], curr_5ple[3], self.pcap_df))
        return self.sessions

    def get_session_values(self):
        self.get_sessions()
        values = []
        for sess in self.sessions:
            values.append([sess.srcIp, sess.srcPort, sess.dstIp, sess.dstPort] )
        return values