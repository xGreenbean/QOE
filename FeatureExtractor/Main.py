import pandas as pd
from containers.Interaction import Interaction
from Features.SampleFactory import SampleFactory
from Generators.CsvGenerator import CsvGenerator
from Generators.SniGenerator import SniGenerator
from Configs import conf
from Features.Vector import Vector
from datafactory import DataFactory
from Streamer import *
import ast
import os
from Breaker import Breaker
import time


def build_csv_features_per_pcap(csv_df, path, id_num, ott, device):
    interaction = Interaction(csv_df)
    all_session = interaction.get_sessions()
    tcp_data = []
    headers = SampleFactory.video_session_request_response_headers()
    tcp_data.append(headers)
    for session in all_session:
        sample = SampleFactory.video_by_request_response_session(session, conf.sni_to_read, 5, 0.05, 250)
        for vector in sample:
            tcp_data.append(vector)
    csv = CsvGenerator(path+device+"_"+ott + "_"+conf.feature_type+"request_response_features_"+id_num+".csv", tcp_data)
    csv.create_file()
    print('Done '+device+" "+ott+" id "+str(id_num))


if __name__ == '__main__':
    start_time = time.time()
    df = pd.read_csv('/home/cyberlab/Desktop/dataset/iphone_youtube/id_4/raw_iphone7_auto_04_19_id_4.csv')
    interaction = Interaction(df)

    for sess in interaction.get_sessions():
        print(sess.to_filter())
        #br = Breaker(sess,0.05,250)
        #vec = Vector(sess).get_vector_feature_by_interval(0.1, conf.app_vid_top_features)
        #vec = Vector(br).get_vector_by_request_response_bins(5, conf.app_vid_top_features)
        #print(conf.app_vid_top_features)
        #print(vec)
    print("--- %s seconds ---" % (time.time() - start_time))


    # DataFactory.export_features('app_request_response')
    # DataFactory.export_features('video_session')
    # DataFactory.export_features('video_request_response')
    # DataFactory.export_features('video_like_request_response')
    # DataFactory.export_features('app_session')
