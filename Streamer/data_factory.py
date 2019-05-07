import os
from data_set_manipulation.ActivityPath import ActivityPath
from SegmentContainer import SegmentContainer
from scapy.all import *

# def produce(data_set_path):
#     #holds the stream splits, streams[index][0] is session pcap for session number index.
#     streams = []
#     #hold the t seconds session splits
#     splits = []
#     for dirName, subdirList, fileList in os.walk(data_set_path):
#         if dirName.split(os.sep)[-1].find('splits') != -1:
#             if len(splits) > 0:
#                 streams.append(list(splits))
#             splits = []
#
#             #find source pcap.
#             source_path = os.path.split(dirName)[0]
#             for fname in os.listdir(source_path):
#                 if fname.endswith('pcap'):
#                     splits.append(os.path.join(source_path, fname))
#             #add splits after.
#             for fname in sorted(fileList):
#                 splits.append(os.path.join(dirName, fname))
#     return streams
data_set_path = "/home/cyberlab/Desktop/dataset"

def produce(data_set_path):
    activity_paths = []
    for dirName, subdirList, fileList in os.walk(data_set_path):
        if os.path.split(dirName)[-1].startswith('id'):
            activity_paths.append(ActivityPath(dirName))
    return activity_paths


def getdownstream(scapy_pcap, client_ip):
    down_stream_pcap = [pkt for pkt in scapy_pcap if pkt[IP].dst == client_ip]
    return down_stream_pcap

produce(data_set_path)
