import pandas as pd
import datetime
"""
 Class PacketContainer holds some data frame df.
"""


class PacketContainer(object):

    def __init__(self, df):
        self.df = df

    """
        function return the df frame the PacketContainer class holds 
    """
    def get_df(self):
        return self.df

    """
         Function split the df to interval in seconds and return list of data frames, each item is interval 
    """
    def split(self, intervals):
        df = self.get_df()
        df = df.dropna(subset=['frame.time_epoch'])
        df['date'] = df['frame.time_epoch'].apply(datetime.datetime.fromtimestamp)
        group_intervals = df.groupby(pd.Grouper(key='date', freq=(str(intervals) + 'S')))
        df_list = []
        counter = 0
        for item in group_intervals:
            df_list.append(item[1])
        return df_list

