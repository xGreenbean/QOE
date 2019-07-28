import os
from containers.Interaction import *
from tools.Breaker import *
from tools.Peaker import *
from features.FeatureAggregation import *
from features.FeaturesCalculation import *
from tools.BigPacket import BigPacket
import pandas as pd
global tshark_pcap_to_csv
global up_link
global down_link
global num_req_res
global first_packet_time
global last_packet_time


up_link = 0
down_link = 1
num_req_res = 2
first_packet_time = 3
last_packet_time = 4
tshark_pcap_to_csv = 'C:\\"Program Files"\\Wireshark\\tshark.exe -r [src] -T fields -e frame.number -e frame.time -e frame.len -e ip.src -e ip.dst -e ip.proto -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e tls.handshake.session_id_length -e tls.handshake.comp_methods_length -e tls.handshake.extension.len -e tls.handshake.cipher_suites_length -e tcp.window_size -e tcp.options.wscale.shift -e tcp.analysis.keep_alive -e tcp.options.mss_val -e tls.handshake.version -e frame.time_delta -e ip.ttl -e tls.handshake.extensions_server_name -e tcp.flags.ack -e tcp.flags.syn -e tcp.ack -e tcp.flags.reset -e frame.time_epoch -e gquic.tag.sni -E header=y -E separator=, -E quote=d -E occurrence=f > [dst]'


class DataFactory:

    # @staticmethod
    # def produce():
    """creates the tshark's csv if dosent exists"""
    @staticmethod
    def make_csv():
        for dirName, subdirList, fileList in os.walk('/home/cyberlab/Desktop/silhouette-trace'):
            for fname in fileList:
                if fname.endswith('.pcap') and fname.replace('.pcap', '.csv') not in fileList:
                    os.system(tshark_pcap_to_csv.replace('[src]', os.path.join(dirName, fname))
                              .replace('[dst]', os.path.join(dirName, fname.replace('.pcap', '.csv'))))

    """cleans up thsark's csv's"""
    @staticmethod
    def clean_csv():
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
            for fname in fileList:
                if fname.endswith('.csv'):
                    os.remove(os.path.join(dirName, fname))

    @staticmethod
    def rename_csv():
        for dirName, subdirList, fileList in os.walk('/home/Desktop/silhouette-trace'):
            for fname in fileList:
                if fname.endswith('.csv') and not fname.startswith('raw'):
                    os.rename(os.path.join(dirName, fname), os.path.join(dirName, 'raw_' + fname))

    @staticmethod
    def clean_features():
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
            for fname in fileList:
                if fname.endswith('.csv') and fname.startswith('features'):
                    os.remove(os.path.join(dirName, fname))

    @staticmethod
    def sessions_to_csv(label_dict=conf.video, peaker=False, breaker=False, path='test.csv'):
        dict_list = []
        for dirName, subdirList, fileList in os.walk(os.path.join(conf.dataset_path)):
            for fname in fileList:
                if fname.endswith('.csv'):

                    df = pd.read_csv(os.path.join(dirName,fname))
                    temp_interaction = Interaction(df)

                    for sess in temp_interaction.get_sessions():
                        dict = {}
                        dict.update([('filter', sess.to_filter()),('source_file', fname),
                                     ('label', sess.get_label(label_dict)), ('sni', sess.get_sni())])

                        dict.update(zip(conf.header_down, FeaturesCalculation(sess.get_flows()[1])
                                          .apply(conf.app_flowdown)))

                        dict.update(zip(conf.header_up, FeaturesCalculation(sess.get_flows()[0])
                                        .apply(conf.app_flowup)))

                        dict.update(zip(conf.header_sess, FeaturesCalculation(sess.get_df())
                                        .apply(conf.app_sess)))
                        if peaker:
                            dict.update(zip(conf.header_peak,
                                        FeatureAggregation(Peaker(sess.get_df())
                                                           .get_dfs())
                                             .apply(conf.app_agg)))
                        if breaker:
                            dict.update(zip(conf.header_break,
                                        FeatureAggregation(Breaker(sess)
                                                           .get_dfs())
                                            .apply(conf.app_agg)))

                        dict_list.append(dict)

        df = pd.DataFrame(dict_list)
        df.to_csv(path)

    # @staticmethod
    def bins_to_csv(label_dict=conf.video, peaker=False, breaker=False, bin_size=5,path='test.csv'):
        dict_list = []
        for dirName, subdirList, fileList in os.walk(os.path.join(conf.dataset_path)):
            print(dirName, fileList)
            for fname in fileList:
                if fname.endswith('.csv'):
                    print(fname)
                    df = pd.read_csv(os.path.join(dirName, fname))
                    temp_interaction = Interaction(df)

                    for sess in temp_interaction.get_sessions():

                        if peaker:
                            for bin in Peaker(sess.get_df()).get_bins(bin_size):
                                if len(bin) != 0:
                                    dict = {}
                                    dict.update([('filter', sess.to_filter()), ('source_file', fname),
                                                 ('label', sess.get_label(label_dict)), ('sni', sess.get_sni())])
                                    dict.update(zip(conf.header_break,
                                                    FeatureAggregation(bin)
                                                    .apply(conf.app_agg)))
                                    dict.update(zip(conf.header_first,
                                                    FeaturesCalculation(bin[0])
                                                    .apply(conf.app_sess)))
                                    dict_list.append(dict)

                        if breaker:
                            for bin in Breaker(sess).get_bins(bin_size):
                                if len(bin) != 0:
                                    dict = {}
                                    dict.update([('filter', sess.to_filter()), ('source_file', fname),
                                                 ('label', sess.get_label(label_dict)), ('sni', sess.get_sni())])
                                    dict.update(zip(conf.header_break,
                                                    FeatureAggregation(bin)
                                                    .apply(conf.app_agg)))
                                    dict.update(zip(conf.header_first,
                                                    FeaturesCalculation(bin[0])
                                                    .apply(conf.app_sess)))
                                    dict_list.append(dict)

        df = pd.DataFrame(dict_list)
        df.to_csv(path)

    def idk_to_csv(sni='fbcdn'):
        for dirName, subdirList, fileList in os.walk(os.path.join(conf.dataset_path)):
            for fname in fileList:
                if fname.endswith('.csv'):
                    bp = BigPacket(csv_path=os.path.join(dirName, fname), interval_size=1, lookup_sni=sni)
                    print(bp.bp_break())


DataFactory.idk_to_csv()

