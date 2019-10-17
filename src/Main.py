import os
from configs.conf import *
from containers.Interaction import *
from features.FeaturesCalculation import *
from features.FeatureAggregation import *
from generators.datafactory import *
from tools.Breaker import *
from tools.Peaker import *
import pandas as pd


if __name__ == '__main__':

    #DataFactory.sessions_to_csv(label_dict=None, peaker=True, breaker=True, path='sess_os_all.csv')

    DataFactory.sessions_to_csv(label_dict=conf.video, peaker=False, breaker=True,
                                path='sess_video_no_video_all_treshold.csv')
    #DataFactory.sessions_to_csv(label_dict=conf.application_sni, peaker=True, breaker=True, video=False,
    #                            path='sess_application_all.csv')


    #DataFactory.bins_to_csv(label_dict=conf.video, peaker=True, breaker=False, bin_size=3, path='video_bin3_peak.csv')
    #DataFactory.bins_to_csv(label_dict=conf.video, peaker=False, breaker=True, bin_size=3, path='video_bin3_break.csv')

    #################################
    #DataFactory.bins_to_csv(label_dict=conf.application_sni, peaker=True, breaker=False, bin_size=3,
    #                        path='app_bin3_peak_new_0.05.csv')
    #DataFactory.bins_to_csv(label_dict=conf.application_sni, peaker=False, breaker=True, bin_size=3,
    #                        path='app_bin3_break_new_agg_0.03.csv')
    #DataFactory.bins_to_csv(label_dict=conf.application_sni, peaker=True, breaker=False, bin_size=5,
    #                        path='app_bin5_peak_new_0.05.csv')
    #DataFactory.bins_to_csv(label_dict=conf.application_sni, peaker=False, breaker=True, bin_size=5,
    #                        path='app_bin5_break_new_agg_0.03.csv')

    #DataFactory.qualities_big_packet_to_csv(csv_path='test_quality_big_packet_up_down_all.csv')
    #DataFactory.qualities_peaks_to_csv(csv_path='test_quality_peaks_up_down_all.csv')
    #DataFactory.qualities_breaker_to_csv(csv_path='test_quality_breaker_up_down_all.csv')

    #DataFactory.qualities_bins_big_packet_to_csv(csv_path='test_quality_big_packet_bins_3.csv', bin_size=3)
    #DataFactory.qualities_bins_big_packet_to_csv(csv_path='test_quality_big_packet_bins_5.csv', bin_size=5)
    #DataFactory.qualities_bins_peaks_to_csv(csv_path='test_quality_peaks_bins_3.csv', bin_size=3)
    #DataFactory.qualities_bins_peaks_to_csv(csv_path='test_quality_peaks_bins_5.csv', bin_size=5)
    #DataFactory.qualities_bins_breaker_to_csv(csv_path='test_quality_breaker_bins_3.csv', bin_size=3)
    #DataFactory.qualities_bins_breaker_to_csv(csv_path='test_quality_breaker_bins_5.csv', bin_size=5)

    #DataFactory.start_delay_to_csv(peaker=True, breaker=False, full_interval=False,
                                   #csv_path='test_delay_Peak_classifier.csv', x_seconds=10)
    #DataFactory.start_delay_to_csv(peaker=False, breaker=True, full_interval=False,
                                   #csv_path='test_delay_Breaker_classifier.csv', x_seconds=10)
    DataFactory.start_delay_to_csv(peaker=False, breaker=True, big_packet=False, full_interval=False,
                                   csv_path='test_delay_big_breaker_quality.csv', x_seconds=10)
