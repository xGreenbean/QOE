from containers.Interaction import *
from Streamer import *
import pandas as pd
from Configs import conf
import os


true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0

for dirName, subdirList, fileList in os.walk(conf.dataset_path):
    for fname in fileList:
        if fname.startswith('raw') and fname.endswith('.csv'):
            interaction_curr = Interaction(pd.read_csv(os.path.join(dirName, fname)))
            streamer_curr = Streamer(interaction_curr, 5, 0.01, 15000)
            video_sessions = streamer_curr.get_video_related_sessions()
            not_video_sessions = streamer_curr.get_not_video_related_sessions()

            print('test started...')
            for video_sess in video_sessions:

                found = False
                for val in conf.video_no_video_sni['video']:

                    if val in video_sess.get_sni():
                        true_positive += 1
                        found = True
                        break
                if not found:
                    false_positive += 1

            for not_video_sess in not_video_sessions:

                found = False

                for val in conf.video_no_video_sni['video']:

                    if val in not_video_sess.get_sni():
                        false_negative += 1
                        found = True
                        break

                if not found:
                    true_negative += 1

            print(os.path.join(dirName, fname))
            print('accuracy', (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative))
            print('precision', (true_positive)/(true_positive + false_positive))