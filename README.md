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
dataset/
(ott,phone) directory/
sample1, sample2,.../
sample_pcap.pcap
sample_video.mp4
SNI.csv
Sessions
Sessions/
session1, session2 ...
session1/
session_pcap.pcap
splits
splits/
session1_first_split.pcap, session1_second_split.pcap
