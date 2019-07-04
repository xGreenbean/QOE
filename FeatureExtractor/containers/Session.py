from containers.Flow import *
from containers.PacketContainer import PacketContainer
from Features.FeaturesCalculation import FeaturesCalculation
"""
Class Session
    define session by 5-tuple: Protocol, ip,port source and destination
    In this class we filter all the packets that belongs to the session,
    then we separate them to flows, upstreams and downstreams
"""


class Session(PacketContainer):

    def __init__(self, protocol, src_port, dst_port, src_ip, dst_ip, csv_file):
        self.srcPort = src_port
        self.srcIp = src_ip
        self.dstIp = dst_ip
        self.dstPort = dst_port
        self.protocol = protocol

        if protocol == "TCP":
            self.df = self.get_all_tcps(csv_file)
        elif protocol == "UDP":
            self.df = self.get_all_udps(csv_file)
        f_up, f_down = self.get_flows()

        self.flow_up = Flow(f_up)
        self.flow_down = Flow(f_down)
        self.connection_opening_time = self.df['frame.time_epoch'].min()

    """
        The function get all the packet in the pcap file, filters the right ip's and then filter all the packets 
        with the right ports values in tcp connection and return the filtered pandas rows 
    """
    def get_all_tcps(self, csv_file):
        filter_ips = self.get_filtered_ips(csv_file)
        tcp_packets = filter_ips.loc[(filter_ips['tcp.srcport'].isin([self.srcPort]) & filter_ips['tcp.dstport'].isin([self.dstPort]))
            | (filter_ips['tcp.srcport'].isin([self.dstPort]) & filter_ips['tcp.dstport'].isin([self.srcPort]))]
        return tcp_packets

    """
        The function get all the packet in the pcap file, filters the right ip's and then filter all the packets 
        with the right ports values in udp connection and return the filtered pandas rows 
    """
    def get_all_udps(self,csv_file):
        filter_ips = self.get_filtered_ips(csv_file)
        udp_packets = filter_ips.loc[(filter_ips['udp.srcport'].isin([self.srcPort]) & filter_ips['udp.dstport'].isin([self.dstPort]))
                     | (filter_ips['udp.srcport'].isin([self.dstPort]) & filter_ips['udp.dstport'].isin([self.srcPort]))]
        return udp_packets

    """
        This function get a pandas object csv_file and return all the rows with the same ip src and dst defining the
         session (A->B,B->A)
    """
    def get_filtered_ips(self,csv_file):
        is_ip = ((csv_file['ip.src'] == self.srcIp) & (csv_file['ip.dst'] == self.dstIp)) | \
                ((csv_file['ip.src'] == self.dstIp) & (csv_file['ip.dst'] == self.srcIp))
        return csv_file[is_ip]

    """
        This function separate all session packets to up flows and down flows based on ip.src defined to the session
    """
    def get_flows(self):
        pd = self.df
        uploads = pd[pd['ip.src'] == self.srcIp]
        downloads = pd[pd['ip.src'] == self.dstIp]
        return uploads, downloads

    def get_session_size(self):
        fc = FeaturesCalculation(self.df)
        return fc.packets_size()

    """
        Function return the sni for the session 
    """
#   csv files from dataset don't have gquic.tag.sni column, Return "None" for now since exporting tcp features only
    def get_sni(self):
        flow_up_df = self.flow_up.get_df()
        if self.protocol == 'TCP':
            sni_filter = "ssl.handshake.extensions_server_name"
        else:
            sni_filter = "gquic.tag.sni"
        df = flow_up_df[flow_up_df[sni_filter].notnull()]
        if len(df) == 0:
            return "None"
        return str(df[sni_filter].iloc[0])

    def to_string(self):
        return [self.protocol, self.srcIp, self.srcPort, self.dstIp, self.dstPort]

    def to_filter(self):
        if self.protocol == 'TCP':
            return ('ip.addr==%s && tcp.port==%d && ip.addr==%s && tcp.port==%d'
                %(self.srcIp, self.srcPort, self.dstIp, self.dstPort))
        else:
            return ('ip.addr==%s && udp.port==%d && ip.addr==%s && udp.port==%d'
                %(self.srcIp, self.srcPort, self.dstIp, self.dstPort))
