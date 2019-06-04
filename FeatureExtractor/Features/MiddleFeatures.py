from Features.FeaturesCalculation import FeaturesCalculation
import numpy as np
import pandas as pd
"""
the class get array of dataframes  , for each dataframe 
we calculate features on that df using FeaturesCalculation 
then we send new vector with values to top Features calculation
"""


class MiddleFeatures:

    def __init__(self, pc):
        self.pc = pc

    def peaks_size(self):
        df_list = self.peak_structure()
        peak_sizes = MiddleFeatures.df_array_to_packet_sizes(df_list)
        return np.array(peak_sizes)

    def first_peak(self):
        print(len(self.peak_structure()))

    def peaks_length(self):
        df_list = self.peak_structure()
        peaks_length = MiddleFeatures.df_array_durations(df_list)
        return np.array(peaks_length)

    def silences_deltas(self):
        df_list = self.peak_structure()
        peak_differences = MiddleFeatures.deltas_between_frames(df_list)
        return np.array(peak_differences)

    def response_request_delta(self):
        df_list = self.pc
        peak_differences = MiddleFeatures.deltas_between_frames(df_list)
        return np.array(peak_differences)

    def response_request_length(self):
        df_list = self.pc
        peaks_length = MiddleFeatures.df_array_durations(df_list)
        return np.array(peaks_length)

    def response_request_sizes(self):
        df_list = self.pc
        peak_sizes = MiddleFeatures.df_array_to_packet_sizes(df_list)
        return np.array(peak_sizes)

    @staticmethod
    def df_array_to_packet_sizes(pc_list):
        packet_sizes_list = []
        for interval in pc_list:
            fc = FeaturesCalculation(interval)
            packet_sizes_list.append(fc.packets_size())
        return packet_sizes_list

    @staticmethod
    def df_array_durations(pc_list):
        durations_list = []
        for interval in pc_list:
            fc = FeaturesCalculation(interval)
            durations_list.append(fc.duration())
        return durations_list

    @staticmethod
    def filter_empty(pc_list):
        non_empty = []
        for interval in pc_list:
            if len(interval) != 0:
                non_empty.append(interval)
        return non_empty

    @staticmethod
    def deltas_between_frames(pc_list):
        frames_differences = []
        for i in range(len(pc_list) - 1):
            max_t = pc_list[i]['frame.time_epoch'].max()
            min_t = pc_list[i + 1]['frame.time_epoch'].min()
            frames_differences.append(min_t - max_t)
        return frames_differences

    def peak_structure(self):
        frames = []
        frames_list = []
        for interval in self.pc:
            if len(interval) != 0:
                frames.append(interval)
            elif len(frames) != 0:
                frames_list.append(pd.concat(frames))
                frames = []

        if len(frames) != 0:
            frames_list.append(pd.concat(frames))
            frames = []
        return frames_list


