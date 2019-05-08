# QOE
This is our final proejct,
hopefully by the end we will have an ML tool for youtube quality detection,
from incrypted traffic.
# sniffing.py
This script sniffs traffic from playing various yt videos at various qualities,
saves them as pcap file.
# test.txt
list of youtube videos , 20 videos that have 140p-1080 quality.
# dir temp
log files for logging exceptions from sniffing.py
# archive temp
old stuff that are no longer used
# Streamer
a light weight classifier for classifying TCP/UDP streams to Video related/non video related classes
#Dataset configuration
dataset/ \n
(ott,phone) directory/ \n
sample1, sample2,.../ \n
sample_pcap.pcap \n
sample_video.mp4 \n
SNI.csv \n 
Sessions \n
Sessions/ \n
session1, session2 ... \n
session1/ \n
session_pcap.pcap \n
splits \n
splits/ \n
session1_first_split.pcap, session1_second_split.pcap \n
