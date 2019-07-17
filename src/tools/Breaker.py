from containers.Session import *
import pandas as pd
from configs import conf
"""
Class Breaker
    Breaks a session into Request and Response pieces,
    A request followed by a response from now one will be called an 'act'. 
    act: like a part of a play, or 'מערכה' in hebrew
"""

class Breaker(object):
    def __init__(self, session, delta_t=conf.delta_t, threshold_t=conf.threshold_t):
        """pandas data frame, represents a session"""
        self.session = session
        """threshold_t, represents GET minimum request size"""
        self.threshold_t = threshold_t
        """delta_t, minimum time between requests"""
        self.delta_t = delta_t

    """returns pandas dataframe[], with each element being a request and its response"""
    def sess_break(self):
        acts = []
        request_start_time = 0
        act = []
        for index, row in self.session.df.iterrows():
            """check for clients packets requests"""
            if row['ip.src'] == self.session.srcIp and row['frame.len'] > self.threshold_t and\
                    (request_start_time == 0 or row['frame.time_epoch'] - request_start_time > self.delta_t):
                if act:
                    acts.append(pd.DataFrame(self.session.df.loc[act]))
                    act.clear()

                request_start_time = row['frame.time_epoch']
                act.append(index)

            else:
                if act:
                    act.append(index)

        if act:
            acts.append(pd.DataFrame(self.session.df.loc[act]))
        return acts

    """returns list of data frames, each data frame is an act"""
    def get_dfs(self):
        return self.sess_break()

    def get_bins(self, bin_size):
        acts = self.sess_break()
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
