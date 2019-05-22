import pandas as pd
from containers.Interaction import Interaction
from Configs import conf


class SniGenerator:

    def __init__(self, labels):
        self.labels = labels

    @staticmethod
    def get_all_sni():
        all_sni_list = []
        for device in conf.Devices:
            for ott in conf.Otts:
                for i in range(conf.numbers_of_id):
                    df = pd.read_csv("C:\\Users\\Saimon\\Desktop\\dataset\\"+device+"_"+ott + "\\Id_" + str(
                        i + 1) + "\\"+device+"_" + ott + "_auto" + str(i + 1) + ".csv")
                    sni_df = SniGenerator.sni_in_df(df)
                    all_sni_list = all_sni_list + sni_df
        return all_sni_list

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

    def save_file(self, file_name, dicts):
        my_file = open(file_name, "w")
        my_file.write(str(dicts))