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
                if fname.endswith('.csv'):
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
    def make_sni(test_type, file_name):
        if test_type == 'app':
            sni_gen = SniGenerator(conf.application_sni)
        if test_type == 'video':
            sni_gen = SniGenerator(conf.video_no_video_sni)
        if test_type == 'video_like':
            sni_gen = SniGenerator(conf.video_videoLike_noVideo)
        all_sni = sni_gen.get_all_sni()
        dict2s = sni_gen.sni_to_label(all_sni)
        sni_gen.save_file(file_name, dict2s)

    @staticmethod
    def export_features(feature_type, is_skip, with_first):
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
            for fname in fileList:
                if fname.endswith('.csv') and fname.startswith('raw'):
                    interaction = Interaction(pd.read_csv(os.path.join(dirName, fname)))
                    all_sessions = interaction.get_sessions()
                    tcp_data = []
                    if feature_type == 'app_session':
                        headers = SampleFactory.session_headers(with_first)
                    elif feature_type == 'app_peak_session_only':
                        headers = SampleFactory.session_peaks_headers(with_first)
                    elif feature_type == 'app_rr_session_only':
                        headers = SampleFactory.session_request_response_headers()
                    elif feature_type == 'video_peak_session_only':
                        headers = SampleFactory.session_peaks_headers(with_first)
                    elif feature_type == 'video_rr_session_only':
                        headers = SampleFactory.session_request_response_headers()
                    elif feature_type == 'app_request_response':
                        headers = SampleFactory.session_request_response_headers()
                    elif feature_type == 'video_session':
                        headers = SampleFactory.session_headers()
                    elif feature_type == 'video_request_response':
                        headers = SampleFactory.session_request_response_headers()
                    elif feature_type == 'video_like_request_response':
                        headers = SampleFactory.session_request_response_headers()
                    tcp_data.append(headers)
                    for session in all_sessions:
                        if feature_type == 'app_session':
                            print(session.to_filter())
                            sample = SampleFactory.application_by_session(session, 0.1, dirName, with_first, is_skip)
                            tcp_data.append(sample)
                        elif feature_type == 'app_peak_session_only':
                            sample = SampleFactory.app_peaks_only(session, 0.1, dirName, with_first, is_skip)
                            tcp_data.append(sample)
                        elif feature_type == 'app_rr_session_only':
                            headers = SampleFactory.app_rr_only(session, 0.05, 250, dirName)
                        elif feature_type == 'video_peak_session_only':
                            headers = SampleFactory.video_peaks_only(session, 0.1, dirName, with_first, is_skip)
                        elif feature_type == 'video_rr_session_only':
                            headers = SampleFactory.video_rr_only(session, 0.05, 250, dirName)
                        elif feature_type == 'app_request_response':
                            sample = SampleFactory.application_by_request_response_session(session, 5, 0.05,
                                                                                     250, dirName)
                            for vector in sample:
                                tcp_data.append(vector)
                        elif feature_type == 'video_session':
                            sample = SampleFactory.video_no_video_by_session(session, 50000,  0.1, dirName)
                            tcp_data.append(sample)
                        elif feature_type == 'video_request_response':
                            sample = SampleFactory.video_by_request_response_session(session,50000, 5, 0.05,
                                                                                     250, dirName)
                            for vector in sample:
                                tcp_data.append(vector)
                        elif feature_type == 'video_like_request_response':
                            sample = SampleFactory.video_video_like_by_request_response_session(session, 50000, 5, 0.05,
                                                                                250, dirName)
                            for vector in sample:
                                tcp_data.append(vector)

                    if feature_type == 'app_session':
                        if with_first:
                            csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'app_with_first_'+str(is_skip)+'_Flag_by_sessions_features')), tcp_data)
                        else:
                            csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'app_by_sessions_features')), tcp_data)
                    elif feature_type == 'app_request_response':
                        csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'app_by_req_res_features')), tcp_data)
                    elif feature_type == 'app_peak_session_only':
                        csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'app_peak_session_features')),
                                           tcp_data)
                    elif feature_type == 'app_rr_session_only':
                        csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'app_rr_session_features')),
                                           tcp_data)
                    elif feature_type == 'video_peak_session_only':
                        csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'video_peak_session_features')),
                                           tcp_data)
                    elif feature_type == 'video_rr_session_only':
                        csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'video_rr_session_features')),
                                           tcp_data)
                    elif feature_type == 'video_session':
                        csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'video_by_session_features')), tcp_data)
                    elif feature_type == 'video_request_response':
                        csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'video_req_res_features')), tcp_data)
                    elif feature_type == 'video_like_request_response':
                        csv = CsvGenerator(os.path.join(dirName, fname.replace('raw', 'video_like_req_res_features')), tcp_data)
                    csv.create_file()

    @staticmethod
    def rename_csv():
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
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
    def print_dates():
        for dirName, subdirList, fileList in os.walk(conf.dataset_path):
            for fname in fileList:
                if fname.endswith('.csv') and fname.startswith('raw'):
                    df = pd.read_csv(os.path.join(dirName, fname))
                    if len(df['frame.time']) > 0:
                        print(os.path.join(dirName, fname))
                        print(df['frame.time'][0])
