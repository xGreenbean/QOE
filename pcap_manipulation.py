import numpy
import pandas as pd
import os
from sklearn import preprocessing

root_dir = os.getcwd()
video_samples = []


class VideoSampleHot:
    def __init__(self, data, labels, 'Hot' = bool ):
        self.data = preprocessing.StandardScaler().fit_transform(data)
        self.labels = [0, 0, 0, 0, 0, 1]
        if labels == 'tiny':
            self.labels = [0, 0, 0, 0, 0, 1]
        if labels == 'small':
            self.labels = [0, 0, 0, 0, 1, 0]
        if labels == 'medium':
            self.labels = [0, 0, 0, 1, 0, 0]
        if labels == 'large':
            self.labels = [0, 0, 1, 0, 0, 0]
        if labels == 'hd720':
            self.labels = [0, 1, 0, 0, 0, 0]
        if labels == 'hd1080':
            self.labels = [1, 0, 0, 0, 0, 0]


class VideoSample:
    def __init__(self, data, labels):
        self.data = preprocessing.StandardScaler().fit_transform(data)
        self.labels = 'tiny'
        if labels == 'tiny':
            self.labels = 'tiny'
        if labels == 'small':
            self.labels = 'small'
        if labels == 'medium':
            self.labels = 'medium'
        if labels == 'large':
            self.labels = 'large'
        if labels == 'hd720':
            self.labels = 'hd720'
        if labels == 'hd1080':
            self.labels = 'hd1080'


def load_pcap_data_hot(sample_size):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".csv"):
                df = pd.read_csv(subdir + '/' + file, usecols=[1], skiprows=[0], header=None, delimiter=' ')
                data = df.values
                data = data * 1.0
                x = len(data) / sample_size
                if x >= 1:
                    data = numpy.array_split(data, x)
                    for sample in data:
                        if len(sample) > sample_size:
                            sample = sample[:sample_size, :]
                        video_samples.append(VideoSampleHot(sample, subdir.split('/')[-1]))
    x = numpy.array([sample.data for sample in video_samples])
    y = numpy.array([sample.labels for sample in video_samples])
    rnd_indices = numpy.random.rand(len(x)) < 0.70
    train_x = x[rnd_indices]
    train_y = y[rnd_indices]
    test_x = x[~rnd_indices]
    test_y = y[~rnd_indices]
    return train_x, train_y, test_x, test_y


def load_pcap_data_non_hot(sample_size):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".csv"):
                df = pd.read_csv(subdir + '/' + file, usecols=[1], skiprows=[0], header=None, delimiter=' ')
                data = df.values
                data = data * 1.0
                x = len(data) / sample_size
                if x >= 1:
                    data = numpy.array_split(data, x)
                    for sample in data:
                        if len(sample) > sample_size:
                            sample = sample[:sample_size, :]
                        video_samples.append(VideoSample(sample, subdir.split('/')[-1]))
    x = numpy.array([sample.data for sample in video_samples])
    y = numpy.array([sample.labels for sample in video_samples])
    rnd_indices = numpy.random.rand(len(x)) < 0.70

    return x,y


