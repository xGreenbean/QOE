import pandas as pd
import datetime
from configs import conf
"""
Class Peaker
    Breaks a dataframe into peak pieces
"""


class Peaker(object):
    """delta_t is time in seconds, to group the dataframe by"""
    def __init__(self, df, delta_t=conf.delta_t):
        self.delta_t = delta_t
        self.df = df

    """returns an array of data frames, where each data frame is a peak"""
    def get_dfs(self):
        self.df = self.df.dropna(subset=['frame.time_epoch'])
        self.df['date'] = self.df['frame.time_epoch'].apply(datetime.datetime.fromtimestamp)
        group_intervals = self.df.groupby(pd.Grouper(key='date', freq=(str(self.delta_t) + 'S')))
        df_list = []
        for item in group_intervals:
            df_list.append(item[1])

        peak = []
        peaks = []
        for interval in df_list:
            if len(interval) > 0:
                peak.append(interval)
            elif len(peak) > 0:
                peaks.append(pd.concat(peak))
                peak = []

        if len(peak) != 0:
            peaks.append(pd.concat(peak))

        return peaks

    def get_bins(self, bin_size):
        peaks = self.get_dfs()
        print(len(peaks))
        bins_list = []
        df = []
        if len(peaks) < bin_size:
            bins_list.append(peaks)
            return bins_list
        for i in range(len(peaks) - bin_size + 1):
            for j in range(bin_size):
                df.append(peaks[i + j])
            bins_list.append(df)
            df = []
        print(len(bins_list))
        return bins_list

    @staticmethod
    def get_bins_h(bin_size, df_list=None):
        peaks = df_list
        bins_list = []
        df = []
        if len(peaks) < bin_size:
            bins_list.append(peaks)
            return bins_list
        for i in range(len(peaks) - bin_size + 1):
            for j in range(bin_size):
                df.append(peaks[i + j])
            bins_list.append(df)
            df = []
        return bins_list