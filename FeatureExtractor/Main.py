import pandas as pd
from containers.Interaction import Interaction
from Features.SampleFactory import SampleFactory
from Generators.CsvGenerator import CsvGenerator
from Generators.SniGenerator import SniGenerator
from Configs import conf
from datafactory import DataFactory
import ast
import os

def build_csv_features_per_pcap(csv_df, path, id_num, ott, device):
    interaction = Interaction(csv_df)
    all_session = interaction.get_sessions()
    tcp_data = []
    headers = SampleFactory.video_session_request_response_headers()
    tcp_data.append(headers)
    for session in all_session:
        sample = SampleFactory.video_by_request_response_session(session, conf.sni_to_read, 5, 0.05, 250)
        for vector in sample:
            tcp_data.append(vector)
    csv = CsvGenerator(path+device+"_"+ott + "_"+conf.feature_type+"request_response_features_"+id_num+".csv", tcp_data)
    csv.create_file()
    print('Done '+device+" "+ott+" id "+str(id_num))


def export_features():
    for device in conf.Devices:
        for ott in conf.Otts:
            if device == "onePlus6" and ott == "download":
                pass
            else:
                for i in range(conf.numbers_of_id):
                    df = pd.read_csv("C:\\Users\\Saimon\\Desktop\\dataset\\" + device + "_" + ott + "\\Id_" + str(
                        i + 1) + "\\"+device+"_" + ott + "_auto" + str(i + 1) + ".csv")
                    build_csv_features_per_pcap(df, "C:\\Users\\Saimon\\Desktop\\dataset\\"+device+"_"+ott+"\\Id_"+str(
                        i+1)+"\\", str(i + 1), ott, device)


def create_sni():
    sni_gen = SniGenerator(conf.video_no_video_sni)
    all_sni = sni_gen.get_all_sni()
    dicts = sni_gen.sni_to_label(all_sni)
    sni_gen.save_file("sni_video_other.txt", dicts)

def what_the_fuck(sni_app__path, dict_to_convert):
    s = open(sni_app__path, 'r').read()
    dicts = ast.literal_eval(s)
    print(dicts)
    found = False

    for key, value in dicts.items():
        for k,val in dict_to_convert.items():
            for v in val:
               if v in key:
                   dicts[key] = k
                   found = True

        if found == False:
            dicts[key] = "Unknown"
        else:
            found = False
    SniGenerator.save_file("sni_video_video_like.txt", dicts)


if __name__ == '__main__':
    DataFactory.export_features('app_session')
    DataFactory.export_features('app_request_response')
    DataFactory.export_features('video_session')
    DataFactory.export_features('video_request_response')
    DataFactory.export_features('video_like_request_response')
