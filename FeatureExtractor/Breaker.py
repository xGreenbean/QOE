from containers.PacketContainer import PacketContainer
import pandas as pd


class Breaker(PacketContainer):
    def __init__(self, session, delta_t, threshold_t):
        self.session = session
        self.threshold_t = threshold_t
        self.delta_t = delta_t

    def sess_break(self):
        requests_responses = []
        request_start_time = 0
        request_response = []
        for index, row in self.session.all_packets.iterrows():
            if row['ip.src'] == self.session.srcIp and row['frame.len'] > self.threshold_t and\
                    (request_start_time == 0 or row['frame.time_epoch'] - request_start_time > self.delta_t):
                if len(request_response) > 0:
                    requests_responses.append(request_response)
                request_response = []

                request_start_time = row['frame.time_epoch']

            else:
                request_response.append(row)

        if len(request_response) > 0:
            requests_responses.append(request_response)
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
            if counter%intervals == 0:
                result = pd.concat(frames)
                request_response_list.append(result)
        return request_response_list
