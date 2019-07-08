from Configs import conf
import pandas as pd
import os

def draw_features(feature_type):
    frames = []
    for dirName, subdirList, fileList in os.walk(conf.dataset_path):
        for fname in fileList:
            if fname.endswith('.csv') and (feature_type in fname):
                df = pd.read_csv(os.path.join(dirName, fname))
                frames.append(df)
                if df.isnull().values.any():
                    print(os.path.join(dirName, fname))

    print("Done Reading")
    result = pd.concat(frames)
    return result
