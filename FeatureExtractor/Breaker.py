from containers.Session import *
import pandas as pd

class Breaker(object):
    def __init__(self, session, delta_t, threshold_t):
        self.session = session
        self.threshold_t = threshold_t
        self.delta_t = delta_t

    def sess_break(self):
        requests_responses =[]
        request_start_time = 0
        request_response = pd.DataFrame(columns=self.session.all_packets.columns)
        for index, row in self.session.all_packets.iterrows():
            if row['ip.src'] == self.session.srcIp and row['frame.len'] > self.threshold_t and\
                    (request_start_time == 0 or row['frame.time_epoch'] - request_start_time > self.delta_t):
                if len(request_response) > 0:
                    requests_responses.append(pd.DataFrame(request_response))
                request_response = request_response.iloc[0:0]
                request_start_time = row['frame.time_epoch']
                request_response = pd.DataFrame(columns=self.session.all_packets.columns)
                request_response.append(row)
            else:
                if len(request_response) > 0:
                    request_response.append(row)
        if len(request_response) > 0:
            requests_responses.append(pd.DataFrame(request_response,self.session.all_packets.columns))
        return requests_responses