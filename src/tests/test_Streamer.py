from containers.Interaction import *
from tools.Streamer import *
import pandas as pd
from configs import conf
import os

delta_s = [2,3,5,7]
delta_t = [0.01, 0.001, 0.0001, 0.05, 0.005, 0.0005]
threshold_p = [150000, 200000, 250000, 300000, 350000]
best_acc = 0
true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0
dict_list = []

for dirName, subdirList, fileList in os.walk('/home/cyberlab/Desktop/silhouette-trace/'):
    for fname in fileList:
        if fname.endswith('.csv'):
            interaction_curr = Interaction(pd.read_csv(os.path.join(dirName, fname)))
            streamer_curr = Streamer(interaction_curr, 5, 0.0001, 250000)
            video_sessions = streamer_curr.get_video_related_sessions()
            not_video_sessions = streamer_curr.get_not_video_related_sessions()

            # print('test started...')
            for video_sess in video_sessions:
                dict = {}
                found = False
                for val in conf.video['video']:

                    if val in video_sess.get_sni():
                            # and video_sess.df['frame.len'].sum() > 1000000: # 1MB
                        true_positive += 1
                        found = True
                        break
                if not found:
                    false_positive += 1
                dict.update(zip(conf.header_streamer, [video_sess.get_sni(), 'yes', fname, video_sess.get_duration(),
                                                       video_sess.get_volume(), video_sess.get_rate(),
                                                       video_sess.get_avg_pkt(),video_sess.get_type(),
                                                       video_sess.get_protocol()]))
                dict_list.append(dict)
            for not_video_sess in not_video_sessions:
                dict = {}
                found = False

                for val in conf.video['video']:

                    if val in not_video_sess.get_sni():
                        false_negative += 1
                        found = True
                        break

                if not found:
                    true_negative += 1
                dict.update(zip(conf.header_streamer, [not_video_sess.get_sni(), 'no', fname, not_video_sess.get_duration(),
                                                       not_video_sess.get_volume(), not_video_sess.get_rate(),
                                                       not_video_sess.get_avg_pkt(), not_video_sess.get_type(),
                                                       not_video_sess.get_protocol()]))
                dict_list.append(dict)

            # print(os.path.join(dirName, fname))
try:
    print('accuracy', (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative))
    print('precision', true_positive/(true_positive + false_positive))
except:
    pass
df = pd.DataFrame(dict_list)
df.to_csv('streamer_results.csv')