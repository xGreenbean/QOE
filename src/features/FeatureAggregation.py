# static variable
skip_first = False
import numpy as np
"""
Class FeatureAggregation:
Preforms feature caculation on lists of dataframes.
Class fields:
df_list - list of data frames.
"""
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
        self.df_list = df_array
        self.sizes = np.zeros(len(self.df_list))
        for index, df in enumerate(self.df_list):
            self.sizes[index] = df['frame.len'].sum()

        self.element_time = np.zeros(len(self.df_list))
        for index, df in enumerate(self.df_list):
            max_t = df['frame.time_epoch'].max()
            min_t = df['frame.time_epoch'].min()
            self.element_time[index] = max_t - min_t

        self.silences = np.zeros(len(self.df_list))
        for i in range(len(self.df_list) - 1):
            max_t = self.df_list[i]['frame.time_epoch'].max()
            min_t = self.df_list[i + 1]['frame.time_epoch'].min()
            self.silences[i] = (min_t - max_t)

        self.lens = np.zeros(len(self.df_list))
        for index, df in enumerate(self.df_list):
            self.lens[index] = len(df)

    def apply(self, feature_list):
        vector = []
        if len(self.df_list) < 2:
            return np.zeros(len(feature_list))
        for feature in feature_list:
            method = getattr(self, feature)
            vector.append(method())
        return vector

    def max_element_size(self):
        return self.sizes.max()

    # def first_peak(self):
    #     return self.middle_features.first_peak_features()

    def min_element_size(self):
        return self.sizes.min()

    def mean_element_size(self):
        return self.sizes.mean()

    def std_element_size(self):
        return self.sizes.std()

    def var_element_size(self):
        return self.sizes.var()

    def sum_element_size(self):
        return self.sizes.sum()

    def max_silence_time(self):
        return self.silences.max()

    def min_silence_time(self):
        min_sil = self.silences
        return np.min(min_sil[np.nonzero(min_sil)])

    def mean_silence_time(self):
        return self.silences.mean()

    def std_silence_time(self):
        return self.silences.std()

    def var_silence_time(self):
        return self.silences.var()

    def sum_silence_time(self):
        return self.silences.sum()

    def max_element_length(self):
        return self.lens.max()

    def min_element_length(self):
        return self.lens.min()

    def mean_element_length(self):
        return self.lens.mean()

    def std_element_length(self):
        return self.lens.std()

    def var_element_length(self):
        return self.lens.var()

    def sum_element_length(self):
        return self.lens.sum()

    def element_count(self):
        return len(self.df_list)

    def max_element_time(self):
        return self.element_time.max()

    def min_element_time(self):
        return self.element_time.min()

    def mean_element_time(self):
        return self.element_time.mean()

    def std_element_time(self):
        return self.element_time.std()

    def var_element_time(self):
        return self.element_time.var()

    def sum_element_time(self):
        return self.element_time.sum()







