import pandas as pd
from containers.Session import *
from containers.PacketContainer import PacketContainer
import time

"""
Class Interaction
    defines interaction between client and the internet,
    -> for our purpose it is a collection of packet containing some interaction,
    that we have recorded.
"""


class Interaction(PacketContainer):

    def __init__(self, df):
        self.clientIP = 0
        self.df = df
        self.sessions = []
        self.sess_dict = {}

    """returns client's ip, we take the ip.src from the first packet where dstport == 443 """
    def get_client_ip(self):
        if self.clientIP != 0:
            return self.clientIP
        else:
            for index, row in self.df.iterrows():
                if row['udp.dstport'] > 0 and row['udp.dstport'] == 443:
                    self.clientIP = row['ip.src']
                elif row['tcp.dstport'] == 443:
                    self.clientIP = row['ip.src']
            return self.clientIP

    """returns List of sessions, a session is a 4 tuple ipsrc,portsrc,ipdst,portdst"""
    ## Maybe should handle better the TCP\UDP seperation.
    def get_sessions(self):
        curr_fiveple = None
        if len(self.sessions) == 0:

            #group by tcp 4ple
            unique_tcps = (self.df[(self.df['tcp.dstport'] == 443) & (self.df['ip.src'] == self.get_client_ip())]
            .groupby(['ip.src','tcp.srcport','ip.dst','tcp.dstport']))

            #group by udp 4ple
            unique_udps = (self.df[(self.df['udp.dstport'] == 443) & (self.df['ip.src'] == self.get_client_ip())]
            .groupby(['ip.src', 'udp.srcport', 'ip.dst', 'udp.dstport']))

            #add tcpc sessions
            for sess in unique_tcps.groups.keys():

                new_session = Session('TCP', sess[0], sess[1],
                                       sess[2], sess[3], self.df)
                key = ['TCP', sess[0], sess[1],
                       sess[2], sess[3]]
                self.sessions.append(new_session)
                #add sessions to Interactions dictionry
                self.sess_dict[(''.join(str(x) + ' ' for x in key))] = new_session

            for sess in unique_udps.groups.keys():

                new_session = Session('UDP', sess[0], sess[1],
                                       sess[2], sess[3], self.df)
                key = ['UDP', sess[0], sess[1],
                       sess[2], sess[3]]
                self.sess_dict[(''.join(str(x) + ' ' for x in key))] = new_session
                self.sessions.append(new_session)
        print(self.sess_dict.keys())
        return self.sessions

    """returns sessions values"""
    def get_session_values(self):
        self.get_sessions()
        values = []
        for sess in self.sessions:
            values.append([sess.srcIp, sess.srcPort, sess.dstIp, sess.dstPort])

        return values

    """returns a sessions coressponding to a session key"""
    def get_session(self, sess_key):
        if self.sess_dict[sess_key]:
            return self.sess_dict[sess_key]

    """
    input: data frame row
    output: a string representing the row. ie port's and ip's.
    """
    def get_session_string(self, row):
        if row['ip.src'] == self.get_client_ip():
            if row['tcp.srcport'] > 0:
                curr_fiveple = ['TCP', row['ip.src'], row['tcp.srcport'], row['ip.dst'], row['tcp.dstport']]
            else:
                curr_fiveple = ['UDP', row['ip.src'], row['udp.srcport'], row['ip.dst'], row['udp.dstport']]

        elif row['tcp.srcport'] > 0:
            curr_fiveple = ['TCP', row['ip.dst'], row['tcp.dstport'], row['ip.src'], row['tcp.srcport']]
        else:
            curr_fiveple = ['UDP', row['ip.dst'], row['udp.dstport'], row['ip.src'], row['udp.srcport']]

        return ''.join(str(x) + ' ' for x in curr_fiveple)
