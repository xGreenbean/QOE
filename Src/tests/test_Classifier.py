from generators.datafactory import DataFactory
from tools.Classifier import Classifier
import os
import pandas as pd

test_path = "C:\\Users\\Saimon\\Desktop\\datase"

def count_tcp_videos(df):
    #df = df[(df['label'] == 'video')]
    df = df[(df['filter'].str.contains("tcp"))]
    print(len(df))

def count_udp_videos():
    pass

def get_labels_file(df):
    return df[['label']]

counter  = 0
def test_classifer():
    for dirName, subdirList, fileList in os.walk(test_path):
            for fname in fileList:
                print(fname)
                print(dirName)
                if 'features' in fname and fname.endswith('.csv'):
                    df = pd.read_csv(dirName + "\\" + fname)
                    count_tcp_videos(df)
                    #c = Classifier(dirName + "\\" + fname)



if __name__ == '__main__':
    test_classifer()
