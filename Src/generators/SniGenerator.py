import pandas as pd
from containers.Interaction import Interaction
from configs import conf
global data_set_path
import os

data_set_path = conf.dataset_path
"""
Class Create an sni to label file based on labels the class gets
The file is in a dictionary format, Each SNI tells what he means by the label.
"""


class SniGenerator:
    def __init__(self, labels):
        self.labels = labels

    """
        Function return all sni's we have in the dataset
    """
    @staticmethod
    def get_all_sni():
        all_sni_list = []
        for dirName, subdirList, fileList in os.walk(data_set_path):
            for fname in fileList:
                print(fname)
                if fname.endswith('.csv') and 'features' not in fname:
                    df = pd.read_csv(os.path.join(dirName, fname))
                    sni_df = SniGenerator.sni_in_df(df)
                    all_sni_list = all_sni_list + sni_df
        return all_sni_list

    """
    Function gets a data frame df and extract from it all the sni's
    """
    @staticmethod
    def sni_in_df(df):
        interaction = Interaction(df)
        all_sessions = interaction.get_sessions()

        all_sni = []
        for session in all_sessions:
            all_sni.append(session.get_sni())
        return all_sni

    def sni_to_label(self, sni_list):
        dicts = {}
        keys = sni_list
        for sni in keys:
            dicts[sni] = self.find_sni_to_value(sni)
        return dicts

    def find_sni_to_value(self, sni):
        found_value = False
        sni_value = ""
        for key, value in self.labels.items():
            for item in value:
                if item in sni:
                    sni_value = key
                    found_value = True
                    break

        if found_value == False:
            sni_value = "Other"
        return sni_value

    @staticmethod
    def save_file(file_name, dicts):
        my_file = open(file_name, "w")
        my_file.write(str(dicts))
