#! /usr/bin/env python
from scapy.all import *

#holds the streams in the 5 seconds interval.
streams = {}

#quaduple that represent a video-related stream.
ott_streams = []

#list of pcap file name's.
cuttings = []
stream_cuttings = []
connenction_open_times = []
#TCP flags
FIN = 0x01
SYN = 0x02
RST = 0x04
PSH = 0x08
ACK = 0x10
URG = 0x20
ECE = 0x40
CWR = 0x80

original_pcap = rdpcap("iphone7_auto_04_19_id_1.pcap")
start_time = original_pcap[0].time
original_pcap = None

my_dir = os.listdir("cuttings")
for pcap_file_path in my_dir:
    stream_cuttings.append(cuttings)
    cuttings = []
    for pcap_stream_cuttings_files in os.listdir("cuttings\\" + pcap_file_path):
        if pcap_stream_cuttings_files.startswith('out'):
            cuttings.append(rdpcap("cuttings\\" + pcap_file_path + "\\" + pcap_stream_cuttings_files))

    for stream in stream_cuttings:
        if len(stream) > 0:
            if len(stream[0]) > 0:
                print((stream[0][0].time - start_time))
        for pcap in stream:
            total_payloads = 0
            if len(pcap) > 0:
                pkt_key = [pcap[0][IP].src, pcap[0].sport, pcap[0][IP].dst, pcap[0].dport]
            for pkt in pcap:
                total_payloads += len(pkt)
                #Bingo!
                if total_payloads > 100000:
                    if pkt_key not in ott_streams:
                        ott_streams.append(pkt_key)
                    # pkt_key[3] = 443
                    # if pkt_key not in ott_streams:
                    #     ott_streams.append(pkt_key)
        streams = {}
print(ott_streams)