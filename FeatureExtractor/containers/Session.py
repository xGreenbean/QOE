from containers.Flow import *

"""
Class Session
    define session by 5-tuple: Protocol, ip,port source and destination
    In this class we filter all the packets that belongs to the session,
    then we separate them to flows, upstreams and downstreams
"""


class Session:

    def __init__(self, protocol,srcPort, dstPort, srcIp, dstIp, csvFile):
        self.srcPort = srcPort
        self.srcIp = srcIp
        self.dstIp = dstIp
        self.dstPort = dstPort
        self.protocol = protocol
        if protocol == "TCP":
            self.all_packets = self.get_all_tcps(csvFile)
        elif protocol == "UDP":
            self.all_packets = self.get_all_udps(csvFile)
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

    def to_print(self):
        return [self.protocol, self.srcIp, self.srcPort, self.dstIp, self.dstPort]