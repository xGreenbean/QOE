import pandas as pd
import datetime
"""
 Class PacketContainer holds some data frame df.
"""


class PacketContainer(object):

    def __init__(self, data_frame):
        self.df = data_frame

    """
        function return the df frame the PacketContainer class holds 
    """
    def getSample(self):
        return self.data_frame

    """
         Function split the df to interval in seconds and return list of data frames, each item is interval 
    """
    def split(self, intervals):
        df = self.getSample()
        df['date'] = df['frame.time_epoch'].apply(datetime.datetime.fromtimestamp)
        print(df['date'])
        group_intervals = df.groupby(pd.Grouper(key='date', freq=(str(intervals) + 'S')))
        df_list = []
        counter = 0
        for item in group_intervals:
            df_list.append(item[1])
        return df_list

