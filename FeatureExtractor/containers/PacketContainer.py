import pandas as pd

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
        df['frame.time'] = (df['frame.time']).str[:-17]
        df['date'] = pd.to_datetime(df['frame.time'])
        group_intervals = df.groupby(pd.Grouper(key='date', freq=(str(intervals) + 'S')))
        df_list = []
        for df in group_intervals:
            df_list.append(df[1])
        return df_list
