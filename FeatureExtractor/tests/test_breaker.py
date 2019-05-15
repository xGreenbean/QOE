from Breaker import *
from containers.Interaction import *

pcap_csv_path = '/home/cyberlab/Desktop/test/testw.csv'
interaction = Interaction(pd.read_csv(pcap_csv_path))

for sess in interaction.get_sessions():
    rrs_df = Breaker(sess, 0.1, 250).sess_break()
    for rr_df in rrs_df:
        print(len(rrs_df), rr_df[0].values)
        break