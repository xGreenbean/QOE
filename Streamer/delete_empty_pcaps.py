#just for expiriments
from scapy.all import *
import os
#delte empty pcaps

my_dir = sorted(os.listdir("cuttings"))
for pcap_file_path in my_dir:
    for pcap_stream_cuttings_files in sorted(os.listdir("cuttings/" + pcap_file_path)):
        if pcap_stream_cuttings_files.startswith('out'):
            if len(rdpcap("cuttings/" + pcap_file_path + "/" + pcap_stream_cuttings_files)) == 0:
                path_to_remove = "cuttings/" + pcap_file_path + "/" + pcap_stream_cuttings_files
                os.system('rm -r ' + path_to_remove)
