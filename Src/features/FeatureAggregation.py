# static variable
skip_first = False
import numpy as np

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

Request Response features:
       responses requests mean
       responses requests min
       responses requests max
       responses requests std
       Number Of responses requests

       responses requests inter arrival time std
       responses requests inter arrival time mean
       responses requests inter arrival time min
       responses requests inter arrival time max
"""

class FeatureAggregation:
    def __init__(self, df_array):
        self.df_array = df_array

    def max_element_size(self):
        sizes = np.zeros(shape=(1,len(self.df_array)))
        for index, df in enumerate(self.df_array):
            sizes[index] = df['frame.len'].sum()
        return sizes.max()

    # def first_peak(self):
    #     return self.middle_features.first_peak_features()

    def min_element_size(self):
        sizes = np.zeros(shape=(1, len(self.df_array)))
        for index, df in enumerate(self.df_array):
            sizes[index] = df['frame.len'].sum()
        return sizes.min()

    def mean_element_size(self):
        sizes = np.zeros(shape=(1, len(self.df_array)))

        for index, df in enumerate(self.df_array):
            sizes[index] = df['frame.len'].sum()
        return sizes.mean()


    def std_element_size(self):
        sizes = np.zeros(shape=(1, len(self.df_array)))

        for index, df in enumerate(self.df_array):
            sizes[index] = df['frame.len'].sum()

        return sizes.mean()


    def max_silence_time(self):
        silences = np.zeros(shape=(1, len(self.df_array) - 1))

        for i in range(len(self.df_array) - 1):
            max_t = self.df_array[i]['frame.time_epoch'].max()
            min_t = self.df_array[i + 1]['frame.time_epoch'].min()
            silences[i] = (min_t - max_t)

        return silences.max()

    def min_silence_time(self):
        silences_deltas = self.middle_features.silences_deltas()
        if np.size(silences_deltas) == 0:
            return 0
        if TopFeatures.skip_first:
            silences_deltas = silences_deltas[1:]
        return silences_deltas.min()


    def mean_silence_time(self):
        silences_deltas = self.middle_features.silences_deltas()
        if np.size(silences_deltas) == 0:
            return 0
        if TopFeatures.skip_first:
            silences_deltas = silences_deltas[1:]
        return silences_deltas.mean()


    def std_silence_time(self):
        silences_deltas = self.middle_features.silences_deltas()
        if np.size(silences_deltas) == 0:
            return 0
        if TopFeatures.skip_first:
            silences_deltas = silences_deltas[1:]
        return silences_deltas.std()


    def max_peak_length(self):
        peaks_length = self.middle_features.peaks_length()
        if np.size(peaks_length) == 0:
            return 0
        if TopFeatures.skip_first:
            peaks_length = peaks_length[1:]
        return peaks_length.max()


    def min_peak_length(self):
        peaks_length = self.middle_features.peaks_length()
        if np.size(peaks_length) == 0:
            return 0
        if TopFeatures.skip_first:
            peaks_length = peaks_length[1:]
        return peaks_length.min()


    def mean_peak_length(self):
        peaks_length = self.middle_features.peaks_length()
        if np.size(peaks_length) == 0:
            return 0
        if TopFeatures.skip_first:
            peaks_length = peaks_length[1:]
        return peaks_length.mean()


    def std_peak_length(self):
        peaks_length = self.middle_features.peaks_length()
        if np.size(peaks_length) == 0:
            return 0
        if TopFeatures.skip_first:
            peaks_length = peaks_length[1:]
        return peaks_length.std()


    # --------------------------------------------

    def peaks_count(self):
        peaks = self.middle_features.peaks_size()
        if len(peaks) != 0 and TopFeatures.skip_first:
            peaks = peaks[1:]
        return len(peaks)


    def max_response_request(self):
        peaks_size = self.middle_features.response_request_sizes()
        if np.size(peaks_size) == 0:
            return 0
        return peaks_size.max()


    def min_response_request(self):
        peaks_size = self.middle_features.response_request_sizes()
        if np.size(peaks_size) == 0:
            return 0
        return peaks_size.min()


    def mean_response_request(self):
        peaks_size = self.middle_features.response_request_sizes()
        if np.size(peaks_size) == 0:
            return 0
        return peaks_size.mean()


    def std_response_request(self):
        peaks_size = self.middle_features.response_request_sizes()
        if np.size(peaks_size) == 0:
            return 0
        return peaks_size.std()


    def max_response_request_delta_time(self):
        silences_deltas = self.middle_features.response_request_delta()
        if np.size(silences_deltas) == 0:
            return 0
        return silences_deltas.max()


    def min_response_request_delta_time(self):
        silences_deltas = self.middle_features.response_request_delta()
        if np.size(silences_deltas) == 0:
            return 0
        return silences_deltas.min()


    def mean_response_request_delta_time(self):
        silences_deltas = self.middle_features.response_request_delta()
        if np.size(silences_deltas) == 0:
            return 0
        return silences_deltas.mean()


    def std_response_request_delta_time(self):
        silences_deltas = self.middle_features.response_request_delta()
        if np.size(silences_deltas) == 0:
            return 0
        return silences_deltas.std()


    def request_response_count(self):
        return len(self.middle_features.response_request_sizes())


    def max_request_response_length(self):
        request_response_length = self.middle_features.response_request_length()
        if np.size(request_response_length) == 0:
            return 0
        if TopFeatures.skip_first:
            request_response_length = request_response_length[1:]
        return request_response_length.max()


    def min_request_response_length(self):
        request_response_length = self.middle_features.response_request_length()
        if np.size(request_response_length) == 0:
            return 0
        if TopFeatures.skip_first:
            request_response_length = request_response_length[1:]
        return request_response_length.min()


    def mean_request_response_length(self):
        request_response_length = self.middle_features.response_request_length()
        if np.size(request_response_length) == 0:
            return 0
        if TopFeatures.skip_first:
            request_response_length = request_response_length[1:]
        return request_response_length.mean()


    def std_request_response_length(self):
        request_response_length = self.middle_features.response_request_length()
        if np.size(request_response_length) == 0:
            return 0
        if TopFeatures.skip_first:
            request_response_length = request_response_length[1:]
        return request_response_length.std()