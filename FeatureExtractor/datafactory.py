import os
import shutil
from Generators.SniGenerator import *
from Features.SampleFactory import  *

global tshark_pcap_to_csv
tshark_pcap_to_csv = 'tshark -r [src] -T fields -e frame.number -e frame.time -e frame.len -e ip.src -e ip.dst -e ip.proto -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e ssl.handshake.session_id_length -e ssl.handshake.comp_methods_length -e ssl.handshake.extension.len -e ssl.handshake.cipher_suites_length -e tcp.window_size -e tcp.options.wscale.shift -e tcp.analysis.keep_alive -e tcp.options.mss_val -e ssl.handshake.version -e frame.time_delta -e ip.ttl -e ssl.handshake.extensions_server_name -e tcp.flags.ack -e tcp.flags.syn -e tcp.ack -e tcp.flags.reset -e frame.time_epoch -e gquic.tag.sni -E header=y -E separator=, -E quote=d -E occurrence=f > [dst]'


class DataFactory:

    # @staticmethod
    # def produce():
    """creates the tshark's csv if dosent exists"""
    @staticmethod
    def make_csv():
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
            for fname in fileList:
                if fname.endswith('.pcap') and fname.replace('.pcap', '.csv') not in fileList:
                    os.system(tshark_pcap_to_csv.replace('[src]', os.path.join(dirName, fname))
                              .replace('[dst]', os.path.join(dirName, fname.replace('.pcap', '.csv'))))

    """cleans up thsark's csv's"""
    @staticmethod
    def clean_csv():
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
            for fname in fileList:
                if fname.endswith('.csv') and not fname.find('SNI'):
                    os.remove(os.path.join(dirName, fname))

    """remvoves old 'sessions' directories from dataset"""
    @staticmethod
    def clean_sessions():
        for dirName, subdirList, fileList in os.walk(conf.data_set_path):
            if dirName.split(os.sep)[-1] == 'sessions':
                shutil.rmtree(dirName)

    @staticmethod
    def clean_SNI():
        for dirName, subdirList, fileList in os.walk(conf.data_set_path):
            for fname in fileList:
                if fname.endswith('.csv') and 'SNI' in fname:
                    os.remove(os.path.join(dirName, fname))

    """creates sni txt file"""
    @staticmethod
    def make_sni(test_type):
        if test_type == 'app':
            sni_gen = SniGenerator(conf.application_sni)
        if test_type == 'video':
            sni_gen = SniGenerator(conf.video_no_video_sni)
        all_sni = sni_gen.get_all_sni()
        dict2s = sni_gen.sni_to_label(all_sni)
        sni_gen.save_file("sni_video_other.txt", dict2s)

    @staticmethod
    def export_features():
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
            for fname in fileList:
                if fname.endswith('.csv') and fname.startswith('raw'):
                    interaction = Interaction(pd.read_csv(os.path.join(dirName, fname)))
                    all_session = interaction.get_sessions()
                    tcp_data = []
                    headers = SampleFactory.video_session_request_response_headers()
                    tcp_data.append(headers)
                    for session in all_session:
                        if session.protocol == "TCP":
                            sample = SampleFactory.video_by_request_response_session(session, conf.sni_to_read, 0.05,
                                                                                     250)
                            tcp_data.append(sample)
                        if session.protocol == "UDP":
                            sample = SampleFactory.video_by_request_response_session(session, conf.sni_to_read, 0.05,
                                                                                     250)
                    csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'features')), tcp_data)
                    csv.create_file()

    @staticmethod
    def rename_csv():
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
            for fname in fileList:
                if fname.endswith('.csv'):
                    os.rename(os.path.join(dirName, fname), os.path.join(dirName, 'raw_' + fname))

    @staticmethod
    def clean_features():
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
            for fname in fileList:
                if fname.endswith('.csv') and fname.startswith('features'):
                    os.remove(os.path.join(dirName, fname))


