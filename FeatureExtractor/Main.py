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

if __name__ == '__main__':
    csv_file = pd.read_csv("testw.csv")
    extract_features(csv_file)


