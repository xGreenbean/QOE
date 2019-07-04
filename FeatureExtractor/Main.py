import pandas as pd
from containers.Interaction import Interaction
from Configs import conf
from datafactory import DataFactory
from Streamer import *
import ast
import os
from Breaker import Breaker
import time

if __name__ == '__main__':
    df = pd.read_csv('/home/ehud/Desktop/dataset/Iphone_youtube/id_4/iphone7_auto_04_19_id_4.csv')
    test = Interaction(df)
