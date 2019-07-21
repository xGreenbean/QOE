import pandas as pd
import numpy as np
import datetime
import os
import pickle
global video,data
data = '/home/ehud/Desktop/dataset/Iphone_youtube/'
video = ["nflxvideo", "fbcdn", "googlevideo", "cdnistagram", "cnnios-f.akamaihd.net", "video.twimg.com"]

class Dataset():
    def __init__(self, df):
        self.sni_dict = {}
        self.df = df
        self.tcps_down = (df[df['tcp.srcport'] == 443]
                     .groupby(['ip.src', 'tcp.srcport', 'ip.dst', 'tcp.dstport']))
        self.tcps_up = (df[df['tcp.dstport'] == 443]
                   .groupby(['ip.src', 'tcp.srcport', 'ip.dst', 'tcp.dstport']))
        self.udps_down = (df[df['udp.srcport'] == 443]
                     .groupby(['ip.src', 'udp.srcport', 'ip.dst', 'udp.dstport']))
        self.udps_up = (df[df['udp.dstport'] == 443]
                   .groupby(['ip.src', 'udp.srcport', 'ip.dst', 'udp.dstport']))
        self.set_dict()
        self.set_xy()

    def set_dict(self):

        for name, tcp_df in self.tcps_up:
            key = self.get_key(tcp_df.iloc[0])
            value = self.get_sni(tcp_df, 'TCP')
            self.sni_dict[key] = value

        for name, udp_df in self.udps_up:
            key = self.get_key(udp_df.iloc[0])
            value = self.get_sni(udp_df, 'UDP')
            self.sni_dict[key] = value

    def get_label(self, row, volume):
        sni = self.sni_dict[self.get_key(row)]
        if (True in [(x in sni) for x in video]) and (volume > 1000000): # volume > 1MB
            return 1
        else:
            return 0

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
    def set_xy(self):
        dict_list = []
        sources = [self.tcps_down, self.udps_down]
        for source in sources:
            for name, tcp_df in source:
                # dropping packets with len of > 1500 like in the papper.
                volume = tcp_df['frame.len'].sum()
                tcp_df = tcp_df[tcp_df['frame.len'] < 1500]
                tcp_df['date'] = tcp_df['frame.time_epoch']. \
                    apply(datetime.datetime.fromtimestamp)  # convert epoch to datetime.
                # divide to 60S intervals
                group_intervals = [item[1] for item in tcp_df.groupby(pd.Grouper(key='date', freq=('60S')))]
                for time_group in group_intervals:
                    if len(time_group) > 0:

                        time_group['frame.time_epoch'] = Dataset.map(time_group['frame.time_epoch'], 1499)
                        # arr = np.zeros((1500, 1500))
                        mults = (time_group['frame.time_epoch'].astype(int)*
                        time_group['frame.len'].astype(int))
                        unique, counts = np.unique(mults, return_counts=True)
                        pic_dic = dict(zip(unique, counts))

                        try:
                            label = self.get_label(time_group.iloc[0], volume)
                            pic_dic['label'] = label
                            dict_list.append(dict(pic_dic))
                            pic_dic.clear()
                        except:
                            pass
        b = []
        if os.path.exists('filename.pickle'):
            with open('filename.pickle', 'rb') as handle:
                try:
                    b = pickle.load(handle)
                except EOFError:
                    pass

        with open('filename.pickle', 'wb') as handle:
            if len(b) > 0:
                dict_list.extend(b)
            pickle.dump(dict_list, handle, protocol=pickle.HIGHEST_PROTOCOL)

def extract():
    if os.path.exists('filename.pickle'):
        os.remove('filename.pickle')
    else:
        print("Can not delete the file as it doesn't exists")
    csvs = []

    for dirName, subdirList, fileList in os.walk(data):
        csvs.extend([os.path.join(dirName, fname) for fname in fileList if fname.endswith('.csv')])
    print('starting...')
    for index,file in enumerate(csvs):
        print(index/ len(csvs),'% done')
        df = pd.read_csv(file)
        Dataset(df)

    with open('filename.pickle', 'rb') as handle:
        b = pickle.load(handle)
        for curr_dict in b:
            arr = np.zeros(1500*1500)
            for key, value in curr_dict.items():
                if key != 'label':
                    arr[key] = value
            print(arr.reshape((1500,1500)))
extract()