<<<<<<< HEAD
<<<<<<< HEAD
from containers.PacketContainer import PacketContainer


class Flow(PacketContainer):
=======
=======
from containers.PacketContainer import PacketContainer
>>>>>>> develop-features


<<<<<<< HEAD
>>>>>>> 62529f38d293bd5e4c20e28ed0cb457625c63b74
=======
class Flow(PacketContainer):
>>>>>>> develop-features

    def __init__(self, flow_packets):
        self.df = flow_packets

<<<<<<< HEAD
<<<<<<< HEAD
    def getSample(self):
        return self.df

=======
    """
    Return unbiased standard deviation of the packet flow time deltas.
    Normalized by N-1 by default. This can be changed using the ddof argument - pandas
    """
    def std_time_delta(self):
        if len(self.df['frame.time_delta']) < 2:
            return 0
        return self.df['frame.time_delta'].std()

    def get_df(self):
        return self.df

    """ Size of all packets in bytes """
    def size(self):
        if len(self.df['frame.len']) == 0:
            return 0
        return self.df['frame.len'].sum()

    """ Amount of packets """
    def __len__(self):
        return len(self.df)

    """ Variance of packet size """
    def sizevar(self):
        if len(self.df) < 2:
            return 0
        return self.df['frame.len'].var()

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

    """ """
    def get_mean_ttl(self):
        if len(self.df) == 0:
            return 0
        if len(self.df) == 1:
            return self.df['ip.ttl'].values[0]
        return self.df['ip.ttl'].mean()

    """
    Peak features:
           peak mean
           peak min
           peak max
           peak std
           Number Of peaks

           peak inter arrival time std
           peak inter arrival time mean
           peak inter arrival time min
           peak inter arrival time max

    """
    def peak_features(self):

        self.df['tcp.ack'].fillna(0)

        p_df = self.df[self.df['tcp.flags.reset'] == False]

        """ Add a column stating whether a certain packet represents a peak """
        self.df['isPeak'] = np.where(self.df['frame.time_delta'] > 0.05, True, False)

        """ A DataFrame containing only peak representing packets """
        peak_df = self.df[self.df['isPeak'] == True]

        """ Getting rid of RST packets which cause undesired behaviour (negative ack diffs)"""
        peak_df = peak_df[peak_df['tcp.flags.reset'] == False]

        """ For every trailing couple of peak representing packets (rows) compute the difference """
        peak_diff_ack = peak_df['tcp.ack'].diff()

        """ Peak inter arrival times """
        piat = peak_df['frame.time_epoch'].diff()

        """ Remove first value since peaks are num (representing) packets - 1 """
        peak_diff_ack = peak_diff_ack[1:]

        """ Same for piat """
        piat = piat[1:]

        if len(peak_df) > 0 :
            """ Features """

            peak_mean = 0
            peak_min = 0
            peak_max = 0
            peak_std = 0
            num_of_peaks = 0
            piat_mean = 0
            piat_min = 0
            piat_max = 0
            piat_std = 0


            if len(peak_diff_ack) > 0:
                if len(peak_diff_ack) == 1:
                    peak_mean = peak_diff_ack.values[0]
                    peak_min = peak_diff_ack.min()
                    peak_max = peak_diff_ack.max()
                    num_of_peaks = len(peak_diff_ack)
                else:
                    peak_mean = peak_diff_ack.mean()
                    peak_min = peak_diff_ack.min()
                    peak_max = peak_diff_ack.max()
                    peak_std = peak_diff_ack.std()
                    num_of_peaks = len(peak_diff_ack)

            if len(piat) > 0:
                if len(piat) == 1:
                    piat_mean = piat.values[0]
                    piat_min = piat.min()
                    piat_max = piat.max()
                else:
                    piat_mean = piat.mean()
                    piat_min = piat.min()
                    piat_max = piat.max()
                    piat_std = piat.std()

            feature_arr = np.array([peak_mean, peak_min, peak_max, peak_std, num_of_peaks, piat_mean, piat_min, piat_max, piat_std])

        else:
            feature_arr = np.zeros(9)

        return feature_arr


    """
    TCP keep alive packet count
    """
    def num_keep_alive(self):
        # print repr(self.df['tcp.analysis.keep_alive_ack'])
        ka_df = self.df[self.df['tcp.analysis.keep_alive'] == True]
        ans = len(ka_df)
        return ans





>>>>>>> 62529f38d293bd5e4c20e28ed0cb457625c63b74
=======
    def getSample(self):
        return self.df

>>>>>>> develop-features
