import pandas as pd
from containers.Interaction import Interaction
from Features.Sample import Sample
from Generators.CsvGenerator import CsvGenerator
from Generators.SniGenerator import SniGenerator
from Configs import conf


def build_csv_features_per_pcap(csv_df, path, id_num, ott, device):
    interaction = Interaction(csv_df)
    all_session = interaction.get_sessions()
    tcp_data = []
    headers = Sample.video_no_video_by_session_headers()
    tcp_data.append(headers)
    for session in all_session:
        if session.protocol == "TCP":
            sample = Sample.application_by_session(session, conf.sni_to_read, 0.1)
            tcp_data.append(sample)

    csv = CsvGenerator(path+device+"_"+ott + "_video_features_"+id_num+".csv", tcp_data)
    csv.create_file()
    print('Done '+device+" "+ott+" id "+ str(id_num))


def export_features():
    for device in conf.Devices:
        for ott in conf.Otts:
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


if __name__ == '__main__':
    export_features()
#   create_sni()


