from tools.Breaker import *
from containers.Interaction import *


def test(pcap_csv_path, pcap_csv_label_path):
    interaction = Interaction(pd.read_csv(pcap_csv_path))
    pd_labels = pd.read_csv(pcap_csv_label_path)

    for sess in interaction.get_sessions():
        rrs_df = Breaker(sess, 0.05, 250).sess_break()
        for rr_df in rrs_df:
            get_number = rr_df['frame.number'].values[0]
            if not (pd_labels['Info'][get_number - 1].startswith('GET') or
                    pd_labels['Info'][get_number - 1].startswith('POST') or
                pd_labels['Info'][get_number - 1].startswith('[TCP Retransmission]')):
                print('test failed at:', pd_labels['Info'][get_number - 1])
                print(pcap_csv_path)
                return False
    return True

pcap_csv_path = '~/Desktop/QOE/test_source_files/test_breaker_'
pcap_csv_label_path = '~/Desktop/QOE/test_source_files/test_breaker_labels_'
for id in [1, 2, 3]:
   if test(pcap_csv_path + str(id) + '.csv', pcap_csv_label_path + str(id) + '.csv'):
       print('test ', id, 'passed')

