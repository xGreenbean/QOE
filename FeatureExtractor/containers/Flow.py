from containers.PacketContainer import PacketContainer

"""
    Class Flow contains a data frames for up/down packets in a session
"""


class Flow(PacketContainer):

    def __init__(self, flow_packets):
        self.df = flow_packets

    def getSample(self):
        return self.df
