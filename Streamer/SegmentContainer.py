from scapy.all import *
from Stream import Stream


class SegmentContainer(Stream):

    def __init__(self, splinters_path):
        self.splinters_path = splinters_path
        self.splinters_it = iter(splinters_path)
        self.curr_splinter = rdpcap(next(self.splinters_it))
        self.connection_opening_time = self.curr_splinter[0].time
        self.ip_src = self.curr_splinter[0][IP].src
        self.ip_dst = self.curr_splinter[0][IP].dst
        self.port_src = self.curr_splinter[0].sport
        self.port_dst = self.curr_splinter[0].dport

    def next(self):
        path = next(self.splinters_it, None)
        if path is None:
            return None
        else:
            self.curr_splinter = rdpcap(path)
            return self.curr_splinter




