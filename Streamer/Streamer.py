import data_factory
from SegmentContainerManipulation import add_sessions_by_server
from SegmentContainerManipulation import add_sessions_by_time

class Streamer(object):
    def __init__(self, activity, threshold):
        self.activity = activity
        self.threshold = threshold

    def get_video_related_streams(self):
        client_ip = self.activity.client_ip
        real_start_time = self.activity.get_start_time()
        start_time = self.activity.get_start_time()
        end_time = self.activity.get_end_time()
        time_interval = end_time - start_time
        total_payloads = 0
        video_treshold = self.threshold
        video_related_streams = set([])

        for x in range(int(time_interval / 5)):
            for index, stream in enumerate(self.activity.streams):
                total_payloads = 0
                flag = 0
                while flag <= 1:
                    curr_stream = stream.curr_splinter
                    if curr_stream is None:
                        flag = 2
                        continue
                    if abs(curr_stream[0].time - start_time) <= 5:
                        for packet in data_factory.getdownstream(curr_stream, client_ip):
                            if (packet.time >= start_time) and (packet.time <= start_time + 5):
                                total_payloads += len(packet)

                        if total_payloads >= video_treshold:
                            video_related_streams.add(stream.to_string())
                            add_sessions_by_server(self.activity.streams, stream, video_related_streams)
                            add_sessions_by_time(self.activity.streams, stream, video_related_streams)
                            self.activity.streams.remove(stream)
                            flag = 2

                    if curr_stream[0].time - start_time <= 0:
                        stream.next()
                    flag += 1
            start_time += 5

        return video_related_streams