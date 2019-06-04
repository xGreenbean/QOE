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
        group_intervals = df.groupby(pd.Grouper(key='date', freq=(str(intervals) + 'S')))
        df_list = []
        for item in group_intervals:
            df_list.append(item[1])
        return df_list

    # def split(self, interval):
    #     counter = 0
    #     df = self.getSample()
    #     peak = []
    #     df_list = []
    #     start_time = df['frame.time_epoch'].min()
    #     end_time = df['frame.time_epoch'].max()
    #     time_interval = end_time - start_time
    #     for t in range(int(time_interval / interval)):
    #         for index, row in df.iterrows():
    #             if abs(row['frame.time_epoch'] - (start_time + t * interval)) <= interval:
    #                 peak.append(index)
    #         df_list.append(pd.DataFrame(df.loc[peak]))
    #         peak.clear()
    #     for bla in df_list:
    #         if len(bla) > 0:
    #             counter += 1
    #     print("#############################3", counter)
    #     return df_list
