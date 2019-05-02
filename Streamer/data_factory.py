import os
from SegmentContainer import SegmentContainer
from scapy.all import *

stream_cuttings = []
cuttings = []
def produce():
    my_dir = sorted(os.listdir("cuttings"))
    for pcap_file_path in my_dir:
        if len(cuttings) > 0:
            stream_cuttings.append(list(cuttings))
        cuttings.clear()
        for pcap_stream_cuttings_files in sorted(os.listdir("cuttings/" + pcap_file_path)):
            if pcap_stream_cuttings_files.startswith('out'):
                cuttings.append("cuttings/" + pcap_file_path + "/" + pcap_stream_cuttings_files)

    streams = []
    for cut in stream_cuttings:
        streams.append(SegmentContainer(cut))
    return streams


def getdownstream(scapy_pcap, client_ip):
    down_stream_pcap = [pkt for pkt in scapy_pcap if pkt[IP].dst == client_ip]
    return down_stream_pcap

