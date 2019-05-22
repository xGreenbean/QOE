<<<<<<< HEAD
import pandas as pd
from containers.Interaction import Interaction
from Features.Sample import Sample
from Generators.CsvGenerator import CsvGenerator
from Generators.SniGenerator import SniGenerator
from Configs import conf
import ast


def build_csv_features_per_pcap(csv_df, path, id_num, ott, device):
    interaction = Interaction(csv_df)
    all_session = interaction.get_sessions()
    tcp_data = []
    headers = Sample.video_session_request_response_headers()
    tcp_data.append(headers)
    for session in all_session:
        if session.protocol == "TCP":
            sample = Sample.video_by_request_response_session(session, conf.sni_to_read, 0.05, 250)
            tcp_data.append(sample)

    csv = CsvGenerator(path+device+"_"+ott + "_"+conf.feature_type+"request_response_features_"+id_num+".csv", tcp_data)
    csv.create_file()
    print('Done '+device+" "+ott+" id "+str(id_num))


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
    dict2s = sni_gen.sni_to_label(all_sni)
    with open(conf.sni_to_read, 'r') as fp:
        file_cont = fp.read()
        dicts = ast.literal_eval(file_cont)
    z = {**dicts, **dict2s}
    sni_gen.save_file("sni_video_other.txt", z)


if __name__ == '__main__':
    export_features()
    #create_sni()
=======
from containers.Session import *
from FeaturesCalculation import *
import pandas as pd


def get_all_sessions(csv_file):
    all_sessions = []
    #mySession = Session("UDP", "42577.0", "443.0", "10.185.33.246", "172.217.22.106", csv_file)
    mySession = Session("TCP", "39600.0", "443.0", "10.185.33.246", "23.23.151.189", csv_file)
    all_sessions.append(mySession)
    return all_sessions


def extract_tcp(session):
    Features = ["fSSL_session_id_len", "fSSL_num_extensions", "fSSL_num_compression_methods",
    "SYN_tcp_scale", "SYN_MSS", "SYN_tcp_winsize", "fcipher_suites", "fSSLv", "size_histogram",
    "fpeak_features", "bpeak_features", "packet_count", "min_packet_size", "max_packet_size",
    "mean_packet_size", "sizevar", "std_fiat", "fpackets", "bpackets", "fbytes", "bbytes", "min_fiat",
    "min_biat", "max_fiat", "max_biat", "std_biat", "mean_fiat", "mean_biat", "min_fpkt", "min_bpkt",
    "max_fpkt", "max_bpkt", "std_fpkt", "std_bpkt", "mean_fpkt", "mean_bpkt", "mean_fttl", "num_keep_alive"]
    feature_session = FeaturesCalculation(session)
    for f in Features:
        method = getattr(feature_session, f)
        print(f + "         " + str(method()))

def extract_udp(session):
    Features = ["size_histogram",
    "fpeak_features", "bpeak_features", "packet_count", "min_packet_size", "max_packet_size",
    "mean_packet_size", "sizevar", "std_fiat", "fpackets", "bpackets", "fbytes", "bbytes", "min_fiat",
    "min_biat", "max_fiat", "max_biat", "std_biat", "mean_fiat", "mean_biat", "min_fpkt", "min_bpkt",
    "max_fpkt", "max_bpkt", "std_fpkt", "std_bpkt", "mean_fpkt", "mean_bpkt", "mean_fttl", "num_keep_alive"]
    feature_session = FeaturesCalculation(session)
    for f in Features:
        method = getattr(feature_session, f)
        print(f + "         " + str(method()))



def extract_features(csv_file):
    all_sessions = get_all_sessions(csv_file)
    for i in range(len(all_sessions)):
        if all_sessions[i].protocol == "TCP":
            extract_tcp(all_sessions[i])
        else:
            extract_udp(all_sessions[i])


def

if __name__ == '__main__':
    csv_file = pd.read_csv("testw.csv")
    extract_features(csv_file)
>>>>>>> 62529f38d293bd5e4c20e28ed0cb457625c63b74


