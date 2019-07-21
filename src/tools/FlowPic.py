
import pandas as pd
import numpy as np
import datetime
import os
from configs import conf
import tensorflow as tf
from sklearn.model_selection import train_test_split
import keras
import keras.layers as layers
from keras.utils.np_utils import to_categorical
from sklearn.metrics import classification_report, confusion_matrix

global video, _id, data_path

data_path = '/home/ehud/PycharmProjects/flowpic/data/'
video = ["nflxvideo", "fbcdn", "googlevideo", "cdnistagram", "cnnios-f.akamaihd.net", "video.twimg.com"]

class Flowpic():
    def __init__(self, np_array, label):
        self.np_array = np_array
        self.label = label

class Interaction():
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
        self.XY = np.empty([0, 1025])

        self.set_xy('TCP')
        self.set_xy('UDP')

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
    def set_xy(self, source):
        if source == 'UDP':
            source = self.udps_down
        else:
            source = self.tcps_down

        for name, tcp_df in source:
            # dropping packets with len of > 1500 like in the papper.
            volume = tcp_df['frame.len'].sum()
            tcp_df = tcp_df[tcp_df['frame.len'] < 1500]
            tcp_df['date'] = tcp_df['frame.time_epoch']. \
                apply(datetime.datetime.fromtimestamp)  # convert epoch to datetime.
            # normalizing packet size, in paper it is unnormalized
            tcp_df['frame.len'] = Interaction.map(tcp_df['frame.len'], 31)

            # divide to 60S intervals
            group_intervals = [item[1] for item in tcp_df.groupby(pd.Grouper(key='date', freq=('60S')))]
            for time_group in group_intervals:
                if len(time_group) > 0:

                    time_group['frame.time_epoch'] = Interaction.map(time_group['frame.time_epoch'], 31)
                    arr = np.zeros((32, 32))
                    np.add.at(arr, (time_group['frame.time_epoch'].astype(int),
                                    time_group['frame.len'].astype(int)), 1)
                    try:
                        label = self.get_label(time_group.iloc[0], volume)
                        arr = arr.flatten()
                        arr = np.insert(arr, 0, label)
                        self.XY = np.vstack([self.XY, arr])
                    except:
                        pass
        print(self.XY)

        prev_xy = np.load("dataset_ours.npy") if os.path.isfile("dataset_ours.npy") else []  # get data if exist
        if len(prev_xy) > 0:
            np.save("dataset_ours", np.vstack([prev_xy, self.XY]))  # save the new
        else:
            np.save("dataset_ours", self.XY)  # save the new

def cnn():
    num_clasess = 2
    FL = np.load('dataset_ours.npy')
    np.random.shuffle(FL)
    video = FL[np.concatenate(FL[:, :1] == 1, axis=0 ) , :]
    non_video = FL[np.concatenate(FL[:, :1] == 0, axis=0 ), :][0:len(video), :]
    FL = np.vstack((video, non_video))
    features = FL[:, 1:]
    labels = FL[:, :1]
    counter = 0
    unique, counts = np.unique(labels, return_counts=True)
    print(dict(zip(unique, counts)))
    test = {}
    train = {}
    train['features'], test['features'], train['labels'], test['labels'] = train_test_split(
        features, labels, test_size=0.2, random_state=0)
    train['features'] = np.reshape(train['features'], (train['features'].shape[0], 32, 32, 1))
    test['features'] = np.reshape(test['features'], (test['features'].shape[0], 32, 32, 1))
    train['labels'] = to_categorical(train['labels'])

    EPOCHS = 10
    BATCH_SIZE = 128

    model = keras.Sequential()

    model.add(layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 1)))
    model.add(layers.MaxPooling2D())

    model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
    model.add(layers.MaxPooling2D())

    model.add(layers.Flatten())

    model.add(layers.Dense(units=120, activation='relu'))

    model.add(layers.Dense(units=84, activation='relu'))

    model.add(layers.Dense(units=num_clasess, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adam(),
                  metrics=['accuracy'])

    model.fit(train['features'], train['labels'], epochs=EPOCHS,  validation_split=0.2,
                        shuffle=True)

    y_pred = model.predict(test['features'])
    score = model.evaluate(test['features'], to_categorical(test['labels']))
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    matrix = confusion_matrix(to_categorical(test['labels']).argmax(axis=1), y_pred.argmax(axis=1))
    print(matrix)

def extract():
    if os.path.exists('dataset_ours.npy'):
        os.remove('dataset_ours.npy')
    else:
        print("Can not delete the file as it doesn't exists")

    csvs = []
    for dirName, subdirList, fileList in os.walk(conf.dataset_path):
        csvs.extend([os.path.join(dirName, fname) for fname in fileList if fname.endswith('.csv')])
    print('starting...')
    for index,file in enumerate(csvs):
        print(index/ len(csvs),'% done')
        df = pd.read_csv(file)
        Interaction(df)
# extract()
cnn()