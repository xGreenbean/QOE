from SegmentContainer import SegmentContainer
from data_set_manipulation.ActivityPath import ActivityPath
from scapy.all import *
from data_set_manipulation.SessionsPath import SessionsPath


class Activity(object):
    def __init__(self, activity_path):
        self.streams = []
        self.stream_paths = []
        self.pcap = rdpcap(activity_path.get_pcap_path())
        self.start_time = self.pcap[0].time
        self.end_time = self.pcap[-1].time

        self.client_ip = self.pcap[0][IP].src
        for session_path in activity_path.get_sessions_path():
            self.stream_paths.append(SessionsPath(session_path))
        for session_path in self.stream_paths:
            self.streams.append(SegmentContainer(session_path.get_splits_path()))


    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time