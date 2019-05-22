from Features.MiddleFeatures import MiddleFeatures
import numpy as np


class TopFeatures:

    def __init__(self, pc_array):
        self.middle_features = MiddleFeatures(pc_array)

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
    def max_peak(self):
        peaks_size = self.middle_features.peaks_size()
        if np.size(peaks_size) == 0:
            return 0
        return peaks_size.max()

    def min_peak(self):
        peaks_size = self.middle_features.peaks_size()
        if np.size(peaks_size) == 0:
            return 0
        return peaks_size.min()

    def mean_peak(self):
        peaks_size = self.middle_features.peaks_size()
        if np.size(peaks_size) == 0:
            return 0
        return peaks_size.mean()

    def std_peak(self):
        peaks_size = self.middle_features.peaks_size()
        if np.size(peaks_size) == 0:
            return 0
        return peaks_size.std()

    def max_silence_time(self):
        silences_deltas = self.middle_features.silences_deltas()
        if np.size(silences_deltas) == 0:
            return 0
        return silences_deltas.max()

    def min_silence_time(self):
        silences_deltas = self.middle_features.silences_deltas()
        if np.size(silences_deltas) == 0:
            return 0
        return silences_deltas.min()

    def mean_silence_time(self):
        silences_deltas = self.middle_features.silences_deltas()
        if np.size(silences_deltas) == 0:
            return 0
        return silences_deltas.mean()

    def std_silence_time(self):
        silences_deltas = self.middle_features.silences_deltas()
        if np.size(silences_deltas) == 0:
            return 0
        return silences_deltas.std()

    def peaks_count(self):
        return len(self.middle_features.peaks_size())