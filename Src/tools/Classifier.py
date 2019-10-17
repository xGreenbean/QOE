from machines import RandomForest
from generators.datafactory import DataFactory
from configs import conf
import pandas as pd
import numpy as np


"""
Class Classifier
    we classify the traffic method from one interaction.
    it's done by using ML to decide whether a session is holding video data or not
    then we can check type(protocol) of a video session and decide the traffic method for the whole interaction 
"""


class Classifier:

    def __init__(self, train_data):
        self.train_dataset = train_data

    """
    Function call Rrf ML algorithem to decide which session in our interaction are video.
    here we use our interaction as the test part onl and the function returns a metrics of the predictions 
    """

    def get_Rrf_prediction(self, feature_file):
        filters = feature_file['filter']
        features = feature_file.drop(['sni', 'filter', 'source_file', 'Unnamed: 0'], axis=1)
        #if 'upstream_ssl_v_0' in features.columns:
        #    features = features.drop(['upstream_ssl_v_0'], axis=1)

        labels = np.array(features[['label_unknown', 'label_video']])
        features = features.drop(['label_unknown', 'label_video'], axis=1)
        features = np.array(features)
        prediction = RandomForest.run_rfr_video_class(0.30, 1256, 41, 42, features, labels, train_features=self.train_dataset)
        tcp_videos, udp_videos = Classifier.find_videos(prediction, filters)
        return Classifier.decision_method(tcp_videos, udp_videos)

    def get_Rrf_prediction_multi(self, feature_file, filters):
        features = feature_file
        labels = np.array(features[['label_unknown', 'label_video']])
        features = features.drop(['label_unknown', 'label_video'], axis=1)
        features = np.array(features)
        prediction = RandomForest.run_rfr_video_class(0.001, 1256, 41, 42, features, labels, train_features=self.train_dataset)
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
                print(type_session)
                if 'tcp' in type_session:
                    tcp_sessions.append(type_session)
                elif 'udp' in type_session:
                    udp_session.append(type_session)
                else:
                    print("ERROR")
        return tcp_sessions, udp_session

    def multi_decisions(self, filter_files=[]):
        df = self.train_dataset
        filters = df['filter']
        sources = df['source_file']
        df = df.drop(['sni', 'filter', 'source_file', 'Unnamed: 0'], axis=1)
        df = df.sample(frac=1)
        df = pd.get_dummies(df)
        df['source_file'] = sources
        df['filter'] = filters
        test_dfs = []
        filters_dfs =[]
        for file in filter_files:
            file = file + '.csv'
            hold_df = df[file == df['source_file']]
            filters_dfs.append(hold_df['filter'])
            test_dfs.append(hold_df)
            df = df[file != df['source_file']]

        df = df.drop(['source_file'], axis=1)
        df = df.drop(['filter'], axis=1)
        self.train_dataset = df
        prediction_dfs = {}
        for i in range(len(test_dfs)):
            holder = test_dfs[i].drop(['source_file', 'filter'], axis=1)
            prediction_dfs.update({filter_files[i]: self.get_Rrf_prediction_multi(holder, filters_dfs[i])})
            print("\n\ndone\n\n")

        return prediction_dfs

    @staticmethod
    def test_correction(dict_results={}):
        pass


if __name__ == '__main__':
    dfa = pd.read_csv('C:\\QOE\\Src\\sess_video_no_video_all_treshold.csv')
    c = Classifier(dfa)
    filtered_files = ['iphone7_facebook_04_19_id_1', 'iphone7_instagram_04_19_id_1', 'iphone7_auto_04_19_id_2',
                      'iphone7_auto_04_19_id_3', 'iphone7_netflix_04_19_id_2', 'onePlus6_facebook_auto_04_19_id_1',
                      'onePlus6_netflix_auto_04_19_id_4', 'onePlus6_netflix_auto_04_19_id_5',
                      'onePlus6_auto_04_19_id_1']
    idk = [
            'iphone_cnn_id_1',
            'iphone7_download_05_19_pt4',
            'iphone7_general_05_19_id_2',
            'iphone_twitter_id_1',
            'xiamoi_cnn_id_2',
            'xiamoi_twitter_id_5',
            'onePlus6_auto_04_19_id_5']


    al = ['iphone7_general_05_19_id_1']
    dic = c.multi_decisions(al)
    print(dic)
    #feature_file = DataFactory.sessions_to_csv(label_dict=conf.video, peaker=False, breaker=True, path=None)
    #print(c.get_Rrf_prediction(), feature_file)