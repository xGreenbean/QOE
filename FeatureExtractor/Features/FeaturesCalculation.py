
import numpy as np
"""
FIX:
"""

"""
Class fields:
sess - Session DataFrame
"""


class FeaturesCalculation:

    def __init__(self, pc):
        self.first_packet = pc.head()
        self.df = pc
        df = self.df
        """ Get client hello """
        self.client_hello_pkt = df[df['tls.handshake.extensions_server_name'].notnull()]
        """ Get SYN packet """
        self.syn_pkt = df[(df['tcp.flags.syn'] == 1) & (df['tcp.flags.ack'] == 0)]

    """ Length in seconds """
    def duration(self):
        fu_fd_df = self.df
        min_t = fu_fd_df['frame.time_epoch'].min()
        max_t = fu_fd_df['frame.time_epoch'].max()
        return max_t - min_t

    """ Size of all packets in bytes """
    def packets_size(self):
        if len(self.df['frame.len']) == 0:
            return 0
        return self.df['frame.len'].sum()

    """ Total number of packets """
    def packet_count(self):
        return len(self.df)

    """ Mean of packet size """
    def mean_packet_size(self):
        fu_fd_df = self.df
        if len(fu_fd_df) == 0:
            return 0
        if len(fu_fd_df) == 1:
            return fu_fd_df['frame.len'].values[0]
        return fu_fd_df['frame.len'].mean()

    """ Variance of packet size """
    def size_var(self):
        fu_fd_df = self.df
        if len(fu_fd_df) < 2:
            return 0
        return fu_fd_df['frame.len'].var()

    """
    Max packet size
    Will return NaN if len(fu_fd_df) == 0
    """
    def max_packet_size(self):
        fu_fd_df = self.df
        if len(fu_fd_df) == 0:
            return 0
        return fu_fd_df['frame.len'].max()

    """ Min packet size """
    def min_packet_size(self):
        fu_fd_df = self.df
        if len(fu_fd_df) == 0:
            return 0
        return fu_fd_df['frame.len'].min()

    """ Min time delta """
    def min_time_delta(self):
        if len(self.df) == 0:
            return 0
        return self.df['frame.time_delta'].min()

    """ Max time delta """
    def max_time_delta(self):
        if len(self.df) == 0:
            return 0
        return self.df['frame.time_delta'].max()

    """ time delta mean """
    def mean_time_delta(self):
        if len(self.df) == 0:
            return 0
        if len(self.df) == 1:
            return self.df['frame.time_delta'].values[0]
        return self.df['frame.time_delta'].mean()

    """ Return unbiased standard deviation of the packet flow time deltas.
        Normalized by N-1 by default. This can be changed using the ddof argument - pandas
    """
    def std_time_delta(self):
        if len(self.df['frame.time_delta']) < 2:
            return 0
        return self.df['frame.time_delta'].std()

    """ Min packet size """
    def min_packet_size(self):
        if len(self.df) == 0:
            return 0

        return self.df['frame.len'].min()

    """ Max packet size """
    def max_packet_size(self):
        if len(self.df) == 0:
            return 0
        return self.df['frame.len'].max()

    """ Std packet size """
    def std_packet_size(self):
        if len(self.df) < 2:
            return 0
        return self.df['frame.len'].std()

    """ Mean packet size """
    def mean_packet_size(self):
        if len(self.df) == 0:
            return 0
        if len(self.df) == 1:
            return self.df['frame.len'].values[0]
        return self.df['frame.len'].mean()

    def upstream_mean_ttl(self):
        if len(self.df) == 0:
            return 0
        if len(self.df) == 1:
            return self.df['ip.ttl'].values[0]
        return self.df['ip.ttl'].mean()

    """
    Packet size histogram of 10 bins
    """
    def size_histogram(self):
        fu_fd_df = self.df
        hist = np.histogram(fu_fd_df['frame.len'], bins=[ 0.,   160.,   320.,   480.,   640.,   800.,   960.,  1120., 1280.,  1440.,  1600. ])
        return hist[0]

    """
    TCP keep alive packet count
    Notice the usage of 'tcp.analysis.keep_alive' which are requests from the client to the server.
    """
    def upstream_num_keep_alive(self):
        ka_df = self.df[self.df['tcp.analysis.keep_alive'] == True]
        ans = len(ka_df)
        return ans

    """
    # TLS versions
    TLS1_V = 0x00000301
    TLS11_V = 0x00000302
    TLS12_V = 0x00000303
    Client to server - SSL version array
    """
    def upstream_ssl_v(self):
        if not self.client_hello_pkt.empty:
            ssl_version = self.client_hello_pkt['tls.handshake.version'].iloc[0]
            return ssl_version
        return 0

    """
    Cipher suites length
    """
    def upstream_cipher_suites(self):
        if not self.client_hello_pkt.empty:
            cipher_suites = self.client_hello_pkt['tls.handshake.cipher_suites_length'].iloc[0]/2
            return cipher_suites
        return 0

    """
    Return the SYN packets TCP window size value
    """
    def syn_tcp_win_size(self):
        win_size_val = self.syn_pkt['tcp.window_size']
        if not win_size_val.empty:
            return win_size_val.iloc[0]
        return 65535

    """
    Get the SYN packet Max Segment Size.
    If MSS is not set return 1500 - IPv4 header (20 bytes) - TCP header (20 bytes)
    """
    def syn_mss(self):
        mss = self.syn_pkt['tcp.options.mss_val']
        if not mss.empty:
            return mss.iloc[0]
        return 1460

    """
    Return the SYN packets TCP scale value
    """
    def syn_tcp_scale(self):
        scale_val = self.syn_pkt['tcp.options.wscale.shift']
        if not scale_val.empty:
            return scale_val.iloc[0]
        return 0

    """
    Client hello TLS number of compression methods
    """
    def upstream_ssl_num_compression_methods(self):
        df = self.client_hello_pkt
        if not df.empty:
            return df['tls.handshake.comp_methods_length'].iloc[0]
        return 0

    """
    Client hello SSL Session id length
    """
    def upstream_ssl_session_id_len(self):
        df = self.client_hello_pkt
        if not df.empty:
            return df['tls.handshake.session_id_length'].iloc[0]
        return 0

    """
    The number of SSL extensions in the client hello packet
    """
    def upstream_ssl_num_extensions(self):
        return "plop"



