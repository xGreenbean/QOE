import os
import shutil

global data_set_path, tshark_pcap_to_csv
data_set_path = '/home/cyberlab/Desktop/dataset/'
tshark_pcap_to_csv = 'tshark -r [src] -T fields -e frame.number -e frame.time -e frame.len -e ip.src -e ip.dst -e ip.proto -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e ssl.handshake.session_id_length -e ssl.handshake.comp_methods_length -e ssl.handshake.extension.len -e ssl.handshake.cipher_suites_length -e tcp.window_size -e tcp.options.wscale.shift -e tcp.analysis.keep_alive -e tcp.options.mss_val -e ssl.handshake.version -e frame.time_delta -e ip.ttl -e ssl.handshake.extensions_server_name -e tcp.flags.ack -e tcp.flags.syn -e tcp.ack -e tcp.flags.reset -e frame.time_epoch -e gquic.tag.sni -E header=y -E separator=, -E quote=d -E occurrence=f > [dst]'


class DataFactory:

    # @staticmethod
    # def produce():
    #
    #
    """creates the tshark's csv if dosent exists"""
    @staticmethod
    def make_csv():
        for dirName, subdirList, fileList in os.walk(data_set_path):
            for fname in fileList:
                if fname.endswith('.pcap') and fname.replace('.pcap', '.csv') not in fileList:
                    os.system(tshark_pcap_to_csv.replace('[src]', os.path.join(dirName, fname))
                              .replace('[dst]', os.path.join(dirName, fname.replace('.pcap', '.csv'))))

    """cleans up thsark's csv's"""
    @staticmethod
    def clean_csv():
        for dirName, subdirList, fileList in os.walk(data_set_path):
            for fname in fileList:
                if fname.endswith('.csv') and not fname.find('SNI'):
                    os.remove(os.path.join(dirName, fname))

    """remvoves old 'sessions' directories from dataset"""
    @staticmethod
    def clean_sessions():
        for dirName, subdirList, fileList in os.walk(data_set_path):
            if dirName.split(os.sep)[-1] == 'sessions':
                shutil.rmtree(dirName)

