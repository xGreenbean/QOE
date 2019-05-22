from containers.Flow import *
<<<<<<< HEAD
<<<<<<< HEAD
from containers.PacketContainer import PacketContainer
=======

>>>>>>> 62529f38d293bd5e4c20e28ed0cb457625c63b74
=======
from containers.PacketContainer import PacketContainer
>>>>>>> develop-features
"""
Class Session
    define session by 5-tuple: Protocol, ip,port source and destination
    In this class we filter all the packets that belongs to the session,
    then we separate them to flows, upstreams and downstreams
"""


<<<<<<< HEAD
<<<<<<< HEAD
class Session(PacketContainer):

    def __init__(self, protocol, src_port, dst_port, src_ip, dst_ip, csv_file):
        self.srcPort = src_port
        self.srcIp = src_ip
        self.dstIp = dst_ip
        self.dstPort = dst_port
        self.protocol = protocol
        if protocol == "TCP":
            self.all_packets = self.get_all_tcps(csv_file)
        elif protocol == "UDP":
            self.all_packets = self.get_all_udps(csv_file)
=======
class Session:
=======
class Session(PacketContainer):
>>>>>>> develop-features

    def __init__(self, protocol, src_port, dst_port, src_ip, dst_ip, csv_file):
        self.srcPort = src_port
        self.srcIp = src_ip
        self.dstIp = dst_ip
        self.dstPort = dst_port
        self.protocol = protocol
        if protocol == "TCP":
            self.all_packets = self.get_all_tcps(csv_file)
        elif protocol == "UDP":
<<<<<<< HEAD
            self.all_packets = self.get_all_udps(csvFile)
>>>>>>> 62529f38d293bd5e4c20e28ed0cb457625c63b74
=======
            self.all_packets = self.get_all_udps(csv_file)
>>>>>>> develop-features
        f_up, f_down = self.find_uploads_downloads()
        self.flow_up = Flow(f_up)
        self.flow_down = Flow(f_down)
        self.connection_opening_time = self.all_packets['frame.time_epoch'].min()

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
    def find_uploads_downloads(self):
        pd = self.all_packets
        uploads = pd[pd['ip.src'] == self.srcIp]
        downloads = pd[pd['ip.src'] == self.dstIp]
        return uploads, downloads

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> develop-features
    def getSample(self):
        return self.all_packets

    """
        Function return the sni for the session 
    """
#   csv files from dataset don't have gquic.tag.sni column, Return "None" for now since exporting tcp features only
    def get_sni(self):
        flow_up_df = self.flow_up.getSample()
        if self.protocol == 'TCP':
            sni_filter = "tls.handshake.extensions_server_name"
        else:
            sni_filter = "gquic.tag.sni"
            return "None"
        df = flow_up_df[flow_up_df[sni_filter].notnull()]
        if len(df) == 0:
            return "None"
        return str(df[sni_filter].iloc[0])

<<<<<<< HEAD
=======
>>>>>>> 62529f38d293bd5e4c20e28ed0cb457625c63b74
=======
>>>>>>> develop-features
    def to_print(self):
        return [self.protocol, self.srcIp, self.srcPort, self.dstIp, self.dstPort]