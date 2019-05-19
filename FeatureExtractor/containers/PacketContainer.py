import pandas as pd


class PacketContainer(object):

    def __init__(self, data_frame):
        self.df = data_frame


    def getSample(self):
        return self.data_frame

    def split(self, intervals):
        df = self.getSample()
        df['frame.time'] = (df['frame.time']).str[:-17]
        df['date'] = pd.to_datetime(df['frame.time'])
        group_intervals = df.groupby(pd.Grouper(key='date', freq=(str(intervals) + 'S')))
        df_list = []
        for df in group_intervals:
            df_list.append(df[1])
        return df_list
