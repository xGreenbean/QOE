#! /usr/bin/env python
from scapy.all import *
import data_factory
from SegmentContainerManipulation import add_sessions_by_server
from SegmentContainerManipulation import add_sessions_by_time
from Activity import Activity


data_set_path = "/home/cyberlab/Desktop/dataset"





activities = []
activity_paths = data_factory.produce(data_set_path)
for activity_path in activity_paths:
    if activity_path.path.find('youtube/id_3') != -1:
        activities.append(Activity(activity_path))

for activity in activities:
    client_ip = activity.client_ip
    real_start_time = activity.get_start_time()
    start_time = activity.get_start_time()
    end_time = activity.get_end_time()
    time_interval = end_time - start_time
    total_payloads = 0
    video_treshold = 1000
    video_related_streams = set([])

    for x in range(int(time_interval / 5)):
        for index, stream in enumerate(activity.streams):
            total_payloads = 0
            flag = 0
            while flag <= 1:
                curr_stream = stream.curr_splinter
                if curr_stream is None:
                    flag = 2
                    continue
                if abs(curr_stream[0].time - start_time) <= 5:
                    print('hi')
                    for packet in data_factory.getdownstream(curr_stream, client_ip):
                        if (packet.time >= start_time) and (packet.time <= start_time + 5):
                            total_payloads += len(packet)

                    if total_payloads >= video_treshold:
                        video_related_streams.add(stream.to_string())
                        add_sessions_by_server(activity.streams, stream, video_related_streams)
                        add_sessions_by_time(activity.streams, stream, video_related_streams)
                        activity.streams.remove(stream)
                        flag = 2

                if curr_stream[0].time - start_time <= 0:
                    stream.next()
                flag += 1
        start_time += 5

    for stream_string in video_related_streams:
        print(stream_string)
    print(activity.path)
