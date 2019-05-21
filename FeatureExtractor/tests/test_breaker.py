from Breaker import *
from containers.Interaction import *
import os

pcap_csv_path = '~/Desktop/QOE/test_source_filestest_breaker_1.csv'
pcap_csv_label_path = '~/Desktop/QOE/test_source_filesbreaker_test_labels_1.csv'
interaction = Interaction(pd.read_csv(pcap_csv_path))
pd_labels = pd.read_csv(pcap_csv_label_path)

def test(pcap_csv_path, pcap_csv_label_path):
    interaction = Interaction(pd.read_csv(pcap_csv_path))
    pd_labels = pd.read_csv(pcap_csv_label_path)

    for sess in interaction.get_sessions():
        rrs_df = Breaker(sess, 0.05, 250).sess_break()
        for rr_df in rrs_df:
            get_number =rr_df[0]['frame.number']
            if not (pd_labels['Info'][get_number - 1].startswith('GET') or
                    pd_labels['Info'][get_number - 1].startswith('POST')):
                print('test failed at:', pd_labels['Info'][get_number - 1])
                return False
    return True


