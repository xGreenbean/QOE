#! /usr/bin/env python
from scapy.all import *
import data_factory
from SegmentContainerManipulation import add_sessions_by_server
from SegmentContainerManipulation import add_sessions_by_time



client_ip = '10.185.33.245'
original_pcap = rdpcap("iphone7_auto_04_19_id_1.pcap")
real_start_time = original_pcap[0].time
start_time = original_pcap[0].time
end_time = original_pcap[-1].time
original_pcap = None

time_interval = end_time - start_time

unclassified_streams = data_factory.produce()
total_payloads = 0
video_treshold = 100000
bingo = True
video_related_streams = set([])


# for index, stream in enumerate(streams):
#     if len(stream.curr_splinter) > 0:
#         print(stream.curr_splinter[0].time - start_time)
#     else:
#         print(stream.splinters_path)

for x in range(int(time_interval / 5)):
    for index, stream in enumerate(unclassified_streams):
        total_payloads = 0
        flag = 0
        while flag <= 1:
            curr_stream = stream.curr_splinter
            if curr_stream is None:
                flag = 2
                continue
            # print(stream.to_string(), curr_stream[0].time - start_time, 'bla')
            if abs(curr_stream[0].time - start_time) <= 5:

                for packet in data_factory.getdownstream(curr_stream, client_ip):
                    if (packet.time >= start_time) and (packet.time <= start_time + 5):
                        total_payloads += len(packet)

                if total_payloads >= video_treshold:
                    video_related_streams.add(stream.to_string())
                    add_sessions_by_server(unclassified_streams, stream, video_related_streams)
                    add_sessions_by_time(unclassified_streams, stream, video_related_streams)
                    unclassified_streams.remove(stream)
                    flag = 2

            if curr_stream[0].time - start_time <= 0:
                stream.next()
            flag += 1
    start_time += 5

for stream_string in video_related_streams:
    print(stream_string)
