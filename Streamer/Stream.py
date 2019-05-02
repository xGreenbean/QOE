
class Stream(object):
    def __init__(self, ip_src, ip_dst, port_src, port_dst, connection_opening_time):
        self.ip_src = ip_src
        self.ip_dst = ip_dst
        self.port_src = port_src
        self.port_dst = port_dst
        self.connection_opening_time = connection_opening_time

    def to_same_server_over_port_443(self, stream_other):
        return (self.ip_src == stream_other.ip_src and self.ip_dst == stream_other.ip_dst
                and stream_other.port_dst == 443)

    def get_start_time(self):
        return self.connection_opening_time

    def to_string(self):
        return "'" + self.ip_src + "' " + str(self.port_src) + " '" +  self.ip_dst + "' " + str(self.port_dst)