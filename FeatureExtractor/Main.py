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

if __name__ == '__main__':
    #start_time = time.time()
    #df = pd.read_csv('/home/cyberlab/Desktop/dataset/iphone_youtube/id_4')
    #interaction = Interaction(df)

    #for sess in interaction.get_sessions():
        #print(sess.to_filter())
        #br = Breaker(sess, 0.05, 250)
        #df = br.split(5)
        # vec = Vector(sess).get_vector_feature_by_interval(0.1, conf.app_vid_top_features)
        #vec = Vector(br).get_vector_by_request_response_bins(5, conf.app_vid_top_features)
        #print(conf.app_vid_top_features)
        #print(len(vec))
    #print("--- %s seconds ---" % (time.time() - start_time))


    #DataFactory.export_features('app_request_response')
    #DataFactory.export_features('video_session')
    #DataFactory.export_features('video_request_response')
    #DataFactory.export_features('video_like_request_response')
    DataFactory.export_features('app_session',False, True)
    # DataFactory.export_features('app_session', True, True)
    # DataFactory.export_features('app_session', False, False)
    # DataFactory.export_features('app_peak_session_only', False, False)
    # DataFactory.export_features('video_peak_session_only', False, False)
    # DataFactory.export_features('app_rr_session_only', False, False)
    # DataFactory.export_features('video_rr_session_only', False, False)

