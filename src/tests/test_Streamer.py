from containers.Interaction import *
from tools.Streamer import *
import pandas as pd
from configs import conf
import os
def test():
    delta_s = [2,3,5,7]
    delta_t = [0.01, 0.001, 0.0001, 0.05, 0.005, 0.0005]
    threshold_p = [150000, 200000, 250000, 300000, 350000]
    best_acc = 0
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    dict_list = []

    for dirName, subdirList, fileList in os.walk('/home/cyberlab/Desktop/canada/'):
        for fname in fileList:
            if fname.endswith('.csv'):
                interaction_curr = Interaction(pd.read_csv(os.path.join(dirName, fname)))
                streamer_curr = Streamer(interaction_curr, 5, 0.001, 250000)
                streamer_curr.stream()
                video_sessions = streamer_curr.get_video()
                video_like_sessions = streamer_curr.get_video_like()
                no_video_sessions = streamer_curr.get_no_video()

                # print('test started...')
                for video_sess in video_sessions:
                    print('video')
                    curr_dict = {}
                    curr_dict.update(zip(conf.header_streamer, [video_sess.get_sni(), 'yes', fname, video_sess.get_duration(),
                                                                video_sess.get_volume(), video_sess.get_rate(),
                                                                video_sess.get_avg_pkt(), video_sess.get_type(),
                                                                video_sess.get_protocol()]))
                    dict_list.append(curr_dict)
                for not_video_sess in no_video_sessions:
                    print('novideo')
                    curr_dict = {}
                    curr_dict.update(zip(conf.header_streamer, [not_video_sess.get_sni(), 'no', fname, not_video_sess.get_duration(),
                                                                not_video_sess.get_volume(), not_video_sess.get_rate(),
                                                                not_video_sess.get_avg_pkt(), not_video_sess.get_type(),
                                                                not_video_sess.get_protocol()]))
                    dict_list.append(curr_dict)

                for not_video_sess in video_like_sessions:
                    print('videolike')
                    curr_dict = {}
                    curr_dict.update(zip(conf.header_streamer, [not_video_sess.get_sni(), 'like', fname, not_video_sess.get_duration(),
                                                                not_video_sess.get_volume(), not_video_sess.get_rate(),
                                                                not_video_sess.get_avg_pkt(), not_video_sess.get_type(),
                                                                not_video_sess.get_protocol()]))
                    dict_list.append(curr_dict)

    df = pd.DataFrame(dict_list)
    df.to_csv('streamer_results.csv')
test()
df = pd.read_csv('streamer_results.csv')
print(df.head())