from containers.PacketContainer import PacketContainer


class Flow(PacketContainer):

    def __init__(self, flow_packets):
        self.df = flow_packets

    def getSample(self):
        return self.df
