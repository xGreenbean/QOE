import os
from configs.conf import *
from containers.Interaction import *
from features.FeaturesCalculation import *
from features.FeatureAggregation import *
from generators.datafactory import *
from tools.Breaker import *
from tools.Peaker import *
import pandas as pd
if __name__ == '__main__':
    # DataFactory.sessions_to_csv(breaker=True, path='sess_breaker.csv')
    # DataFactory.sessions_to_csv(peaker=True, path='sess_peaker')
    # DataFactory.bins_to_csv(breaker=True, path='bins_breaker.csv')
    # DataFactory.bins_to_csv(peaker=True, path='bin_speaker.csv')
    df = pd.read_csv('/home/cyberlab/Desktop/silhouette-trace/https-240p/https-2ktuvx9hrMw-240p-catnap.txt'
                     ,header=None, usecols=[1, 14], names=[])
    print(df.head())