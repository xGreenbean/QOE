from containers.Interaction import *
from Streamer import *
import pandas as pd


def test_youtube():
    test_interaction = Interaction(pd.read_csv('/home/cyberlab/Desktop/test/testw.csv'))
    test_streamer = Streamer(test_interaction, 1, 5, 100000)
    ground_truth = pd.read_csv('/home/cyberlab/Desktop/test/SNI.csv').drop_duplicates()
    video_values = test_streamer.get_video_related_sessions_values()
    all_sessions = test_interaction.get_session_values()
    output = []
    for sess_value in all_sessions:
        for video_value in video_values:
            if test_equal_values(sess_value, video_value):
                sess_value.append(video_value[4])  # by th
                sess_value.append(video_value[5])  # by time
                sess_value.append(video_value[6])  # by server
                sess_value.append(True)  # predicted

        for index, row in ground_truth.iterrows():
            if test_equals_ground(sess_value, row):
                if len(sess_value) == 4:
                    sess_value.append(False)  # by th
                    sess_value.append(False)  # by time
                    sess_value.append(False)  # by server
                    sess_value.append(False)  # predicted
                sess_value.append(True)  # real
                sess_value.append(row.values[0])

        if len(sess_value) == 4:
            sess_value.append(False)  # by th
            sess_value.append(False)  # by time
            sess_value.append(False)  # by server
            sess_value.append(False)  #predicted

        if len(sess_value) == 8:
            sess_value.append(False)
            sess_value.append('None')

        output.append(sess_value)

    print(output)


def test_equals_ground(value, row):
    return value[0] == row.values[1] and value[1] == row.values[2] and \
           value[2] == row.values[3] and value[3] == row.values[4]


def test_equals_predicted(sess, pred_sess):
    return sess.srcIp == pred_sess.srcIp and sess.srcPort == pred_sess.srcPort and \
           sess.dstIp == pred_sess.dstIp and sess.dstPort == pred_sess.dstPort


def test_equal_values(value, value_other):
    return value[0] == value_other[0] and value[1] == value_other[1] and \
           value[2] == value_other[2] and value[3] == value_other[3]


test_youtube()