from machines import RandomForest
import pandas as pd
import numpy as np


"""
Class Classifier
    we classify the traffic method from one interaction.
    it's done by using ML to decide whether a session is holding video data or not
    then we can check type(protocol) of a video session and decide the traffic method for the whole interaction 
"""


class Classifier:

    def __init__(self, path):
        self.feature_file = pd.read_csv(path)

    """
    Function call Rrf ML algorithem to decide which session in our interaction are video.
    here we use our interaction as the test part onl and the function returns a metrics of the predictions 
    """
    def get_Rrf_prediction(self):
        filters = self.feature_file[['filter']]
        features = self.feature_file.drop(['sni', 'filter', 'source_file', 'Unnamed: 0'], axis=1)
        features = features.sample(frac=1)
        features = pd.get_dummies(features)
        labels = np.array(features[['label_unknown', 'label_video']])
        features = features.drop(['label_unknown', 'label_video'], axis=1)
        features = np.array(features)
        prediction = RandomForest.run_rfr_video(0.30, 1256, 41, 42, features, labels)
        tcp_videos, udp_videos = Classifier.find_videos(prediction, filters)
        return Classifier.decision_method(tcp_videos, udp_videos)

    """
    Function gets lists of tcp and udp sessions which were found as a video session, then based
    on the list sizes we decide the traffic method  
    """
    @staticmethod
    def decision_method(tcp_sessions, udp_sessions):
        tcp_length = len(tcp_sessions)
        udp_length = len(udp_sessions)
        if tcp_length > 1 and udp_length > 1:
            return "TCP multi stream and UDP multi stream{ TCP:" + str(tcp_length) + ", UDP:" + str(udp_length) + "}"
        elif tcp_length > 1 and udp_length == 0:
            return "TCP multi stream { TCP:" + str(tcp_length) + "}"
        elif tcp_length > 1 and udp_length == 1:
            return "TCP multi stream and UDP single stream{ TCP:" + str(tcp_length) + ", UDP:" + str(udp_length) + "}"
        elif tcp_length == 0 and udp_length > 1:
            return "UDP multi stream{ UDP:" + str(udp_length) + "}"
        elif tcp_length == 0 and udp_length == 1:
            return "UDP single stream{ UDP:" + str(udp_length) + "}"
        elif tcp_length == 0 and udp_length == 0:
            return "No video traffic"
        elif tcp_length == 1 and udp_length > 1:
            return "TCP single stream and UDP multi stream{ TCP:" + str(tcp_length) + ", UDP:" + str(udp_length) + "}"
        elif tcp_length == 1 and udp_length == 1:
            return "TCP single stream and UDP single stream{ TCP:" + str(tcp_length) + ", UDP:" + str(udp_length) + "}"
        elif tcp_length == 1 and udp_length == 0:
            return "TCP single stream{ TCP:" + str(tcp_length) + "}"

    """
    Function gets predictions and filter of each session(ip port ip port)
    and find from the prediction which session are predicted as videos and by their index find the right filter
    of this session to decide whether its a tcp session or udp session carrying video traffic
    """
    @staticmethod
    def find_videos(predictions, filters):
        tcp_sessions = []
        udp_session = []
        for i in range(len(predictions)):
            if predictions[i][1] == 1:
                type_session = filters.iloc[i]
                if 'tcp' in type_session[0]:
                    tcp_sessions.append(type_session[0])
                elif 'udp' in type_session[0]:
                    udp_session.append(type_session[0])
                else:
                    print("ERROR")
        return tcp_sessions, udp_session


if __name__ == '__main__':
    c = Classifier('C:\\QOE\\Src\\sess_breaker_c3.csv')
    print(c.get_Rrf_prediction())