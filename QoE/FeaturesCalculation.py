from containers.Flow import Flow
import numpy as np
import numbers

"""
FIX:
"""

"""
Class fields:
sess - Session DataFrame
"""


class FeaturesCalculation:

    def __init__(self, session):
        self.first_packet = session.all_packets.head()
        self.flow_up = session.flow_up
        self.flow_down = session.flow_down
        self.all_flow = session.all_packets

        """ Get client hello """
        fu_df = self.flow_up.get_df()
        self.client_hello_pkt = fu_df[fu_df['tls.handshake.extensions_server_name'].notnull()]
        """ Get SYN packet """
        self.syn_pkt = fu_df[(fu_df['tcp.flags.syn'] == 1) & (fu_df['tcp.flags.ack'] == 0)]


    """ Length in seconds """
    def duration(self):
        fu_fd_df = self.all_flow
        min_t = fu_fd_df['frame.time_epoch'].min()
        max_t = fu_fd_df['frame.time_epoch'].max()
        return max_t - min_t




    """ Size of all packets in bytes """
    def size(self):
        return self.flow_up.size() + self.flow_down.size()

    """ Amount of packets """
    def __len__(self):
        return len(self.flow_up) + len(self.flow_down)

    """ Total number of packets """
    def packet_count(self):
        return len(self)

    """ Mean of packet size """
    def mean_packet_size(self):
        fu_fd_df = self.all_flow
        if len(fu_fd_df) == 0:
            return 0
        if len(fu_fd_df) == 1:
            return fu_fd_df['frame.len'].values[0]
        return fu_fd_df['frame.len'].mean()

    """ Variance of packet size """
    def sizevar(self):
        fu_fd_df = self.all_flow
        if len(fu_fd_df) < 2:
            return 0
        return fu_fd_df['frame.len'].var()

    """
    Max packet size
    Will return NaN if len(fu_fd_df) == 0
    """
    def max_packet_size(self):
        fu_fd_df = self.all_flow
        return fu_fd_df['frame.len'].max()

    """ Min packet size """
    def min_packet_size(self):
        fu_fd_df = self.all_flow
        return fu_fd_df['frame.len'].min()

    """ # Packets in forward direction (fpackets) """
    def fpackets(self):
        return len(self.flow_up)

    """ # Packets in backward direction (bpackets) """
    def bpackets(self):
        return len(self.flow_down)

    """ # Bytes in forward direction (fbytes) """
    def fbytes(self):
        return self.flow_up.size()

    """ # Bytes in backward direction (bbytes) """
    def bbytes(self):
        return self.flow_down.size()

    """ Min forward inter-arrival time (min_fiat) """
    def min_fiat(self):
        return self.flow_up.min_time_delta()

    """ Min backward inter-arrival time (min_biat) """
    def min_biat(self):
        return self.flow_down.min_time_delta()

    """ Max forward inter-arrival time (max_fiat) """
    def max_fiat(self):
        return self.flow_up.max_time_delta()

    """ Max backward inter-arrival time (max_biat) """
    def max_biat(self):
        return self.flow_down.max_time_delta()

    """ Standard deviation of forward inter- arrival times (std_fiat) """
    def std_fiat(self):
        return self.flow_up.std_time_delta()

    """ Standard deviation of backward inter- arrival times (std_biat) """
    def std_biat(self):
        return self.flow_down.std_time_delta()

    """ Mean forward inter-arrival time (mean_fiat) """
    def mean_fiat(self):
        return self.flow_up.mean_time_delta()

    """ Mean backward inter-arrival time (mean_biat) """
    def mean_biat(self):
        return self.flow_down.mean_time_delta()

    """ Min forward packet length (min_fpkt) """
    def min_fpkt(self):
        return self.flow_up.min_packet_size()

    """ Min backward packet length (min_bpkt) """
    def min_bpkt(self):
        return self.flow_down.min_packet_size()

    """ Max forward packet length (max_fpkt) """
    def max_fpkt(self):
        return self.flow_up.max_packet_size()

    """ Max backward packet length (max_bpkt) """
    def max_bpkt(self):
        return self.flow_down.max_packet_size()

    """ Std deviation of forward packet length (std_fpkt) """
    def std_fpkt(self):
        return self.flow_up.std_packet_size()

    """ Std deviation of backward packet length (std_bpkt) """
    def std_bpkt(self):
        return self.flow_down.std_packet_size()

    """ Mean forward packet length (mean_fpkt)	"""
    def mean_fpkt(self):
        return self.flow_up.mean_packet_size()

    """ Mean backward packet length (mean_bpkt) """
    def mean_bpkt(self):
        return self.flow_down.mean_packet_size()

    """
    Our features
    """

    """
    Discretized upstream TTL values.
    Assuming Two bins: 0-64, 65-128
    """
    def mean_fttl(self):
        if self.flow_up.get_mean_ttl() <= 64:
            return np.array([1,0])
        elif self.flow_up.get_mean_ttl() > 64:
            return np.array([0,1])
        else:
            return np.array([0,0])

    """
    Upstream TTL value.
    No bins
    """
    def mean_fttl_no_bins(self):
        mean_ttl = self.flow_up.get_mean_ttl()
        if isinstance(mean_ttl, numbers.Number):
            return mean_ttl
        return 0

    """ Forward peak features """
    def fpeak_features(self):
        return self.flow_up.peak_features()

    """ Backward peak features """
    def bpeak_features(self):
        return self.flow_down.peak_features()

    """
    Packet size histogram of 10 bins

    The original Ethernet IEEE 802.3 standard defined the minimum Ethernet frame size as 64 bytes
    and the maximum as 1518 bytes.
    The maximum was later increased to 1522 bytes to allow for VLAN tagging.
    The minimum size of an Ethernet frame that carries an ICMP packet is 74 bytes.
    """
    def size_histogram(self):
        fu_fd_df = self.all_flow
        hist = np.histogram(fu_fd_df['frame.len'], bins=[ 0.,   160.,   320.,   480.,   640.,   800.,   960.,  1120., 1280.,  1440.,  1600. ])
        return hist[0]

    """
    TCP keep alive packet count

    If no such packets exist (i.e. 0) This might indicate usage of IExplorer.

    Notice the usage of 'tcp.analysis.keep_alive' which are requests from the client to the server.
    """
    def num_keep_alive(self):

        return self.flow_up.num_keep_alive()

    """
    # TLS versions
    TLS1_V = 0x00000301
    TLS11_V = 0x00000302
    TLS12_V = 0x00000303

    ssl3   tls1  tls11 tls12
    [0,    0,    0,    1]

    Client to server - SSL version array
    """
    def fSSLv(self):
        if not(self.client_hello_pkt.empty):
            ssl_version = self.client_hello_pkt['tls.handshake.version'].iloc[0]
            return ssl_version
        return 0

    """
    Cipher suites length
    0-13, 13-17, 17-24

    Note: Each cipher suite is 2 bytes.
    """
    def fcipher_suites(self):
        if not(self.client_hello_pkt.empty):
            cipher_suites = self.client_hello_pkt['tls.handshake.cipher_suites_length'].iloc[0]/2
            hist = np.histogram(np.array(cipher_suites), bins=[ 0, 13, 17, 24 ])
            return hist[0]
        return [0,0,0]

    """
    Cipher suites length
    No bins, single value
    """
    def fcipher_suites_no_bins(self):
        if not(self.client_hello_pkt.empty):
            cipher_suites = self.client_hello_pkt['tls.handshake.cipher_suites_length'].iloc[0]/2
            return cipher_suites
        return 0

    """
    Return the SYN packets TCP window size value
    """
    def SYN_tcp_winsize(self):
        winsize_val = self.syn_pkt['tcp.window_size']
        if not(winsize_val.empty):
            return winsize_val.iloc[0]
        return 65535

    """
    Get the SYN packet Max Segment Size.

    If MSS is not set return 1500 - IPv4 header (20 bytes) - TCP header (20 bytes)
    """
    def SYN_MSS(self):
        mss = self.syn_pkt['tcp.options.mss_val']
        if not(mss.empty):
            return mss.iloc[0]
        return 1460


    """
    Return the SYN packets TCP scale value
    """
    def SYN_tcp_scale(self):
        scale_val = self.syn_pkt['tcp.options.wscale.shift']
        if not(scale_val.empty):
            return scale_val.iloc[0]
        return 0


    """
    Client hello TLS number of compression methods
    """
    def fSSL_num_compression_methods(self):
        df = self.client_hello_pkt
        if not(df.empty):
            return df['tls.handshake.comp_methods_length'].iloc[0]
        return 0


    """
    Client hello SSL Session id length
    """
    def fSSL_session_id_len(self):
        df = self.client_hello_pkt
        if not(df.empty):
            return df['tls.handshake.session_id_length'].iloc[0]
        return 0

    """
    The number of SSL extensions in the client hello packet

    Notice: using scapy + scapy.ssl_tls
    """
    def fSSL_num_extensions(self):
        return "plop"



