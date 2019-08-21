from containers.Flow import *
import pandas as pd
from containers.PacketContainer import PacketContainer
from features.FeaturesCalculation import FeaturesCalculation
"""
Class Session
    define session by 5-tuple: Protocol, ip,port source and destination
    In this class we filter all the packets that belongs to the session,
    then we separate them to flows, upstreams and downstreams
"""
pd.options.mode.chained_assignment = None


class Session(PacketContainer):

    def __init__(self, protocol, src_ip, src_port, dst_ip, dst_port, df):

        self.srcPort = src_port
        self.srcIp = src_ip
        self.dstIp = dst_ip
        self.dstPort = dst_port
        self.protocol = protocol
        self.streamer_type = 'tobedefined'
        if protocol == "TCP":
            self.df = self.get_all_tcps(df)
        elif protocol == "UDP":
            self.df = self.get_all_udps(df)
        f_up, f_down = self.get_flows()

        self.flow_up = Flow(f_up)
        self.flow_down = Flow(f_down)
        self.connection_opening_time = self.df['frame.time_epoch'].min()

    """
        The function get all the packet in the pcap file, filters the right ip's and then filter all the packets 
        with the right ports values in tcp connection and return the filtered pandas rows 
    """
    def get_all_tcps(self, df):
        filter_ips = self.get_filtered_ips(df)
        tcp_packets = filter_ips.loc[(filter_ips['tcp.srcport'].isin([self.srcPort]) & filter_ips['tcp.dstport'].isin([self.dstPort]))
            | (filter_ips['tcp.srcport'].isin([self.dstPort]) & filter_ips['tcp.dstport'].isin([self.srcPort]))]

        tcp_packets['key'] = self.get_string()
        return tcp_packets

    """
        The function get all the packet in the pcap file, filters the right ip's and then filter all the packets 
        with the right ports values in udp connection and return the filtered pandas rows 
    """
    def get_all_udps(self,df):
        filter_ips = self.get_filtered_ips(df)
        udp_packets = filter_ips.loc[(filter_ips['udp.srcport'].isin([self.srcPort]) & filter_ips['udp.dstport'].isin([self.dstPort]))
                     | (filter_ips['udp.srcport'].isin([self.dstPort]) & filter_ips['udp.dstport'].isin([self.srcPort]))]
        udp_packets['key'] = self.get_string()
        return udp_packets

    """
        This function get a pandas object csv_file and return all the rows with the same ip src and dst defining the
         session (A->B,B->A)
    """
    def get_filtered_ips(self,df):
        is_ip = ((df['ip.src'] == self.srcIp) & (df['ip.dst'] == self.dstIp)) | \
                ((df['ip.src'] == self.dstIp) & (df['ip.dst'] == self.srcIp))
        return df[is_ip]

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
            sni_filter = "tls.handshake.extensions_server_name"
        else:
            sni_filter = "gquic.tag.sni"
        df = flow_up_df[flow_up_df[sni_filter].notnull()]
        if len(df) == 0:
            return "None"
        return str(df[sni_filter].iloc[0])

    def to_string(self):
        return [self.protocol, self.srcIp, self.srcPort, self.dstIp, self.dstPort]

    """returns a string representing the wireshark filter of the session."""
    def to_filter(self):
        if self.protocol == 'TCP':
            return ('ip.addr==%s && tcp.port==%d && ip.addr==%s && tcp.port==%d'
                %(self.srcIp, self.srcPort, self.dstIp, self.dstPort))
        else:
            return ('ip.addr==%s && udp.port==%d && ip.addr==%s && udp.port==%d'
                %(self.srcIp, self.srcPort, self.dstIp, self.dstPort))

    """input: a dictionary, where key is is the label,
        and sni values for it.
        output: a label coresspoding to the sessions sni, based on input dict"""
    def get_label(self,label_dict):
        for key, values in label_dict.items():
            for value in values:
                if value in self.get_sni():
                    return key
            return 'unknown'

    def get_avg_pkt(self):
        return self.df['frame.len'].mean()

    def get_duration(self):
        return self.df['frame.time_epoch'].max() - self.df['frame.time_epoch'].min()

    def get_volume(self):
        return self.df['frame.len'].sum()

    def get_rate(self):
        return self.get_volume()/self.get_duration()

    def get_type(self):
        return self.streamer_type

    def get_protocol(self):
        return self.protocol

    def get_string(self):
        curr_fiveple = [self.protocol, self.srcIp, self.srcPort, self.dstIp, self.dstPort]
        return ''.join(str(x) + ' ' for x in curr_fiveple)