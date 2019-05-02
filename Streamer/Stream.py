from scapy.all import *
class Stream(object):

    def __init__(self, splinters_path):
        self.splinters_path = splinters_path
        self.splinters_it = iter(splinters_path)
        self.curr_splinter = rdpcap(next(self.splinters_it))

    def next(self):
        path = next(self.splinters_it, None)
        if path is None:
            return None
        else:
            self.curr_splinter = rdpcap(path)
            return self.curr_splinter
