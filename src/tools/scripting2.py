import pandas as pd
import numpy as np
import datetime
import os
import pickle
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from collections import Counter
global video, data_path, OTT, file_name

file_name = 'pickle1MB.pickle'
data_path = '/home/cyberlab/Desktop/canada/'
video = ["nflxvideo", "fbcdn", "googlevideo", "cdnistagram", "cnnios-f.akamaihd.net", "video.twimg.com", "vimeocdn",
         "cbp-us.nccp.netflix.com"]
OTT = {
    "netflix": ["nflxvideo", "cbp-us.nccp.netflix.com"],
    "facebook": ["fbcdn"],
    "youtube": ["googlevideo"],
    "instagram": ["cdnistagram"],
    "vimeo" : ["vimeocdn"]
    "cnn" : ["cnnios-f.akamaihd.net"]
    }

udp_grouping = ['ip.src', 'udp.srcport', 'ip.dst', 'udp.dstport']
tcp_grouping = ['ip.src', 'tcp.srcport', 'ip.dst', 'tcp.dstport']


class Interaction:
    def __init__(self, df, fname):
        self.fname = fname
        self.sni_dict = {}
        self.df = df
        self.tcp_down = (df[df['tcp.srcport'] == 443].groupby(tcp_grouping))
        self.tcp_up = (df[df['tcp.dstport'] == 443].groupby(tcp_grouping))
        self.udp_down = (df[df['udp.srcport'] == 443].groupby(udp_grouping))
        self.udp_up = (df[df['udp.dstport'] == 443].groupby(udp_grouping))
        self.set_dict()

    def set_dict(self):
        for prot, _dfs in [('TCP', self.tcp_up), ('UDP', self.udp_up)]:
            for name, _df in _dfs:
                key = self.get_key(_df.iloc[0])
                value = self.get_sni(_df, prot)
                self.sni_dict[key] = value

    def get_video_label(self, row, volume):
        sni = self.sni_dict[self.get_key(row)]
        if (True in [(x in sni) for x in video]) and volume > 1000000: # volume > 1MB
            return 'video'
        else:
            return 'novideo'

    def get_ott_label(self, row, volume):
        sni = self.sni_dict[self.get_key(row)]
        if self.get_video_label(row, volume) == 'video':
            for key, values in OTT.items():
                for value in values:
                    if value in sni:
                        return key
        return 'novideo'


    @staticmethod
    def get_key(row):
        if row['tcp.dstport'] == 443:
            curr_fiveple = ['TCP', row['ip.src'], row['tcp.srcport'], row['ip.dst'], row['tcp.dstport']]
        elif row['tcp.dstport'] > 0:
            curr_fiveple = ['TCP', row['ip.dst'], row['tcp.dstport'], row['ip.src'], row['tcp.srcport']]
        elif row['udp.dstport'] == 443:
            curr_fiveple = ['UDP', row['ip.src'], row['udp.srcport'], row['ip.dst'], row['udp.dstport']]
        elif row['udp.dstport'] > 0:
            curr_fiveple = ['UDP', row['ip.dst'], row['udp.dstport'], row['ip.src'], row['udp.srcport']]

        return ''.join(str(x) + ' ' for x in curr_fiveple)

    @staticmethod
    def get_sni(df, proto):
        if proto == 'TCP':
            sni_filter = "ssl.handshake.extensions_server_name"
        else:
            sni_filter = "gquic.tag.sni"

        temp = df[df[sni_filter].notnull()]
        if len(temp) == 0:
            return "None"

        return str(temp[sni_filter].iloc[0])

    @staticmethod
    # input - dataframe, range to normal dataframe to
    # ouput - normalized df between 0 and range.
    def map(row, range):
        if row.max() - row.min() == 0:
            return 0
        else:
            return range * (row - row.min()) / (row.max() - row.min())

    # Sets the XY and appends it to the dataset
    # XY - np.array, first col is label, rest is the features.
    def export(self):
        pics = []
        sources = [self.tcp_down, self.udp_down, self.udp_up, self.tcp_up]
        for source in sources:
            for name, tcp_df in source:
                tcp_df = tcp_df[np.isfinite(tcp_df['frame.time_epoch'])]
                # dropping packets with len of > 1500 like in the papper.
                volume = tcp_df['frame.len'].sum()
                print(volume)
                tcp_df = tcp_df[tcp_df['frame.len'] < 1500]
                tcp_df['date'] = tcp_df['frame.time_epoch']. \
                    apply(datetime.datetime.fromtimestamp)  # convert epoch to datetime.

                # divide to 60S intervals
                group_intervals = [item[1] for item in tcp_df.groupby(pd.Grouper(key='date', freq='60S'))]
                for time_group in group_intervals:
                    if len(time_group) > 0:
                        curr_pic = []
                        time_group['frame.time_epoch'] = Interaction.map(time_group['frame.time_epoch'], 31)
                        time_group['frame.len'] = Interaction.map(time_group['frame.len'], 31)

                        mults = (time_group['frame.time_epoch'].astype(int) *
                                 time_group['frame.len'].astype(int))

                        plt.scatter(mults)
                        plt.show()

                        unique, counts = np.unique(mults, return_counts=True)
                        pic_dic = dict(zip(unique, counts))

                        arr = np.zeros((32, 32))
                        for key, value in pic_dic.items():
                            if 'label' not in str(key):
                                arr[key] = value

                        try:
                            video_label = self.get_video_label(time_group.iloc[0], volume)
                            ott_label = self.get_ott_label(time_group.iloc[0], volume)
                            curr_pic.extend([video_label, ott_label])
                            pics.append(list(curr_pic))
                            print(','.join(map(str, curr_pic)))
                            curr_pic.clear()
                        except:
                            pass

def produce():
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("Can not delete the file as it doesn't exists")
    csvs = []

    for dirName, subdirList, fileList in os.walk(data_path):
        csvs.extend([os.path.join(dirName, fname) for fname in fileList if fname.endswith('.csv')])
    print('starting...')
    for index, file in enumerate(csvs):
        df = pd.read_csv(file)
        print(file)
        Interaction(df).export()


df = pd.read_csv('/home/cyberlab/Desktop/dataset/iphone_youtube_QOE/id_1/iphone7_youtube_long_05_19_pt1.csv')
Interaction(df).export()