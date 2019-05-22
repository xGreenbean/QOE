from containers.Interaction import *
from Streamer import *
import pandas as pd
import os

youtube_sni_list = ['googlevideo', 'youtube', 'ytimg', 'yt3']
netflix_sni_list = ['neflix', 'nflx']
instagram_sni_list = ['graph.facebook.com', 'facebook', 'i.instagram.com', 'instagram', 'cdninstagram']
facebook_sni_list = ['facebook', 'fbcdn']


def test_youtube(sni_csv_path, pcap_csv_path, th, delta_s, delta_t, sni_list):

    interaction = Interaction(pd.read_csv(pcap_csv_path))
    streamer = Streamer(interaction, delta_t, delta_s, th)
    ground_truth_df = pd.read_csv(sni_csv_path).drop_duplicates()
    predicted_sessions_values = streamer.get_video_related_sessions_values()
    all_sessions_values = interaction.get_session_values()
    output = []

    for sess_value in all_sessions_values:

        for video_value in predicted_sessions_values:
            if test_equal_values(sess_value, video_value):
                # by th, by time, by server, predicted
                sess_value.extend([video_value[4], video_value[5], video_value[6], True])

        for index, row in ground_truth_df.iterrows():
            if len(sess_value) == 4:
                # if were here, it means that this was not classified as video
                # by th, by time, by server, predicted
                sess_value.extend([False, False, False, False])

            if test_equals_ground(sess_value, row):

                if sni_match(sni_list, row.values[0]):
                    # if were here, the session is a video session
                    sess_value.append(True)  # real
                else:
                    sess_value.append(False)
                sess_value.append(row.values[0])

        if len(sess_value) == 8:
            # if were here, session is nor video.
            sess_value.extend([False, 'None'])

        output.append(sess_value)

    true_positive = true_negative = false_positive = false_negative = 0

    for sess in output:
        if sess[7] and sess[8]:
            true_positive += 1
        if sess[7] and not sess[8]:
            false_positive += 1
        if not sess[7] and sess[8]:
            false_negative += 1
        if not sess[7] and not sess[8]:
            true_negative += 1

    accuracy = (true_negative + true_positive) / len(output)
    precision = (true_positive / (true_positive + false_positive))
    f_measure = 2 * precision * accuracy / (accuracy + precision)
    df = pd.DataFrame(output)
    df.columns = ['ipsrc', 'portsrc', 'ipdst', 'portdst', 'by_payload', 'by_time', 'by_server', 'predicted_videp', 'video', 'sni']
    df.to_csv(os.path.join(os.path.split(pcap_csv_path)[0], 'resluts.csv'))

    with open(os.path.join(os.path.split(pcap_csv_path)[0], 'resluts.txt'), 'w') as f:
        f.write('accuracy: %' + str(accuracy) + '\n')
        f.write('precision: %' + str(precision) + '\n')
        f.write('F1 score: ' + str(f_measure) + '\n')
        f.write('th: ' + str(th) + ' delta_t: ' + str(delta_t) + ' delta_s: ' + str(delta_s) + '\n')


def test_equals_ground(value, row):
    return value[0] == row.values[1] and value[1] == row.values[2] and \
           value[2] == row.values[3] and value[3] == row.values[4]


def test_equals_predicted(sess, pred_sess):
    return sess.srcIp == pred_sess.srcIp and sess.srcPort == pred_sess.srcPort and \
           sess.dstIp == pred_sess.dstIp and sess.dstPort == pred_sess.dstPort


def test_equal_values(value, value_other):
    return value[0] == value_other[0] and value[1] == value_other[1] and \
           value[2] == value_other[2] and value[3] == value_other[3]


def sni_match(sni_list, sni_string):
    for sni in sni_list:
        if sni in sni_string:
            return True
        return False

test_youtube('/home/cyberlab/Desktop/test/SNI.csv', '/home/cyberlab/Desktop/test/testw.csv', 1000000, 5, 1, youtube_sni_list)