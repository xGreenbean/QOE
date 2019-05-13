#! /usr/bin/env python
from scapy.all import *
<<<<<<< Updated upstream
my_dir = os.listdir("cuttings")

#holds the streams in the 5 seconds interval.
streams = {}

#quaduple that represent a video-related stream.
ott_streams = []

#list of pcap file name's.
cuttings = []

#TCP flags
FIN = 0x01
SYN = 0x02
RST = 0x04
PSH = 0x08
ACK = 0x10
URG = 0x20
ECE = 0x40
CWR = 0x80

for pcap_file_path in my_dir:
    cuttings.append(rdpcap("cuttings\\" + pcap_file_path))

for index, pcap in enumerate(cuttings):
    print(pcap[0][IP].src)
    for pkt in pcap:
        pkt_key = [pkt[IP].src, pkt[IP].dst, pkt.sport, pkt.dport]
        if streams.get(repr(pkt_key)) is not None:
            streams.get(repr(pkt_key)).append(pkt)
        else:
            streams[repr(pkt_key)] = [pkt]

    for key in streams:
        total_payloads = 0
        for pkt in streams[key]:
            pkt[IP].src
            total_payloads += len(pkt)

        #Bingo!
        if total_payloads > 1000000:
            # print repr(key)
            # print total_payloads
            if key not in ott_streams:
                ott_streams.append(key)

        #check locality in time
        #for now i have decided to drop it.
        #be careful with adding lists or representaions of strings
            # for pkt in pcap:
            #     #connection was opened
            #     if(pkt[TCP].flags and ACK and SYN):
            #         if [pkt[IP].src, pkt[IP].dst, pkt.sport, pkt.dport] not in ott_streams:
            #             ott_streams.append([pkt[IP].src, pkt[IP].dst, pkt.sport, pkt.dport])
        #add to data set one minute forward and one minute backwards

    streams = {}
print(ott_streams )
=======
import data_factory
from SegmentContainerManipulation import add_sessions_by_server
from SegmentContainerManipulation import add_sessions_by_time
from Activity import Activity
load_layer("tls")

pcap_path = "/home/cyberlab/Desktop/dataset/iphone youtube/id_2/iphone7_auto_04_19_id_2.pcap"
scapy_pcap = rdpcap(pcap_path)
scapy_pcap[0].time

>>>>>>> Stashed changes
