
from containers.Session import *
import pandas as pd


class Breaker(object):
    def __init__(self, session, delta_t, threshold_t):
        """pandas data frame, represents a session"""
        self.session = session
        """threshold_t, represents GET minimum request size"""
        self.threshold_t = threshold_t
        """delta_t, minimum time between requests"""
        self.delta_t = delta_t

    """returns pandas dataframe[], with each element being a request and its response"""

    def sess_break(self):
        requests_responses = []
        request_start_time = 0
        request_response = []
        for index, row in self.session.all_packets.iterrows():

            """check for clients packets requests"""
            if row['ip.src'] == self.session.srcIp and row['frame.len'] > self.threshold_t and \
                    (request_start_time == 0 or row['frame.time_epoch'] - request_start_time > self.delta_t):

                if request_response:
                    requests_responses.append(pd.DataFrame(self.session.all_packets.loc[request_response]))
                    request_response.clear()

                request_start_time = row['frame.time_epoch']
                request_response.append(index)

            else:
                if request_response:
                    request_response.append(index)

        if request_response:
            requests_responses.append(pd.DataFrame(self.session.all_packets.loc[request_response]))

        return requests_responses
    
    def getSample(self):
        return self.sess_break()

    def split(self, intervals):
        request_response = self.sess_break()
        counter = 0
        frames = []
        request_response_list = []
        for sample in request_response:
            counter += 1
            frames.append(sample)
            if counter % intervals == 0:
                result = pd.concat(frames)
                request_response_list.append(result)
        return request_response_list