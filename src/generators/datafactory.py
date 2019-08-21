import os
from containers.Interaction import *
from tools.Breaker import *
from tools.Peaker import *
from features.FeatureAggregation import *
from features.FeaturesCalculation import *
from tools.BigPacket import BigPacket
from generators.data_parser import DataParser
import pandas as pd
global tshark_pcap_to_csv
global data_frame
global delay_time
global qualities
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
data_frame = 0
delay_time = 2
qualities = 1
tshark_pcap_to_csv = 'C:\\"Program Files"\\Wireshark\\tshark.exe -r [src] -T fields -e frame.number -e frame.time -e frame.len -e ip.src -e ip.dst -e ip.proto -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e tls.handshake.session_id_length -e tls.handshake.comp_methods_length -e tls.handshake.extension.len -e tls.handshake.cipher_suites_length -e tcp.window_size -e tcp.options.wscale.shift -e tcp.analysis.keep_alive -e tcp.options.mss_val -e tls.handshake.version -e frame.time_delta -e ip.ttl -e tls.handshake.extensions_server_name -e tcp.flags.ack -e tcp.flags.syn -e tcp.ack -e tcp.flags.reset -e frame.time_epoch -e gquic.tag.sni -E header=y -E separator=, -E quote=d -E occurrence=f > [dst]'


class DataFactory:

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

    @staticmethod
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

    @staticmethod #get df
    def qualities_big_packet_to_csv(breaker=False, peaker=False, csv_path='test_big_packet_breaker.csv'):
        full_df = None
        dict_list = []
        sql_file_path = None
        for dirName, subdirList, fileList in os.walk(os.path.join(conf.dataset_path)):
            if 'YouTube' in dirName:
                sni = 'googlevideo'
            else:
                sni = 'nflxvideo'

            for fname in fileList:
                if fname.endswith('.csv'):
                    full_df = pd.read_csv(os.path.join(dirName, fname))
                elif fname.endswith('.mf'):
                    sql_file_path = os.path.join(dirName, fname)

                if full_df is not None and sql_file_path is not None:
                    divided_file_list = DataParser(df=full_df, sql_file=sql_file_path).divide_playbacks()
                    for one_playback in divided_file_list:
                        df = one_playback[data_frame]
                        bp_list = BigPacket(df=df, interval_size=1, lookup_sni=sni).bp_break()
                        qoe = one_playback[qualities]

                        first_time = min(qoe)
                        curr_quality = qoe[first_time]
                        del qoe[first_time]
                        for bp in bp_list:
                            bp_start_time = bp[first_packet_time]
                            bp_end_time = bp[last_packet_time]
                            for time_key, quality in qoe.items():
                                if not (first_time <= bp_start_time and bp_end_time <= time_key):
                                    first_time = time_key
                                    curr_quality = quality
                                    del qoe[first_time]
                                    break
                            curr_df = df[(df['frame.time_epoch'] > bp[first_packet_time]) & (df['frame.time_epoch']
                                                                                             <= bp[last_packet_time])]

                            dict_row = {}
                            dict_row.update([('filter', str(bp[first_packet_time]) + "_" +
                                              str(bp[last_packet_time])), ('source_file', fname),
                                             ('label', curr_quality)])
                            dict_row.update([('bp_num_request_response', bp[num_req_res]),
                                             ('bp_up_link', bp[up_link]), ('bp_down_link', bp[down_link])])

                            dict_row.update(zip(conf.header_quality_bp,
                                                FeaturesCalculation(curr_df).apply(conf.quality_bp)))
                            dict_list.append(dict_row)
                            if peaker:
                                dict_row.update(zip(conf.header_peak, FeatureAggregation(Peaker(curr_df).get_dfs())
                                                    .apply(conf.app_agg)))
                            if breaker:
                                dict_row.update(zip(conf.header_break, FeatureAggregation(Breaker().get_dfs(curr_df))
                                                    .apply(conf.app_agg)))

                    full_df = None
                    sql_file_path = None
        df = pd.DataFrame(dict_list)
        df.to_csv(csv_path)

    @staticmethod
    def qualities_peaks_to_csv(csv_path='test_peaks_peaker_on_session_with_filter.csv'):
        full_df = None
        dict_list = []
        sql_file_path = None
        for dirName, subdirList, fileList in os.walk(os.path.join(conf.dataset_path)):
            if 'YouTube' in dirName:
                sni = 'googlevideo'
            else:
                sni = 'nflxvideo'

            for fname in fileList:
                if fname.endswith('.csv'):
                    full_df = pd.read_csv(os.path.join(dirName, fname))
                elif fname.endswith('.mf'):
                    sql_file_path = os.path.join(dirName, fname)

                if full_df is not None and sql_file_path is not None:
                    divided_file_list = DataParser(df=full_df, sql_file=sql_file_path).divide_playbacks()
                    for one_playback in divided_file_list:
                        df = one_playback[data_frame]
                        qoe = one_playback[qualities]
                        sess_list = Interaction(df).get_sessions()
                        #sess_sni_list = []
                        peak_list = []
                        for sess in sess_list:
                            if sni in sess.get_sni():
                                peak_list.extend([x for x in Peaker(sess.get_df()).get_dfs() if x['frame.len']
                                                 .sum() > 1000])
                        #df = pd.concat(sess_sni_list)
                        peak_list.sort(key=lambda x: x.iloc[0]['frame.time_epoch'])
                        #df.sort_values('frame.time_epoch')
                        #peak_list = Peaker(df).get_dfs()

                        curr_time = min(qoe)
                        curr_quality = qoe[curr_time]
                        del qoe[curr_time]
                        is_first = False
                        for peak in peak_list:
                            peak_start_time = peak['frame.time_epoch'].min()
                            peak_end_time = peak['frame.time_epoch'].max()
                            for time_key, quality in qoe.items():
                                if not (curr_time <= peak_start_time and peak_end_time <= time_key) and is_first:
                                    curr_time = time_key
                                    curr_quality = quality
                                    del qoe[curr_time]
                                    break

                            is_first = True
                            dict_row = {}
                            dict_row.update([('filter', "_"), ('source_file', fname),
                                             ('label', curr_quality), ('peak_size', peak['frame.len'].sum())])

                            dict_row.update(zip(conf.header_quality_peaks, FeaturesCalculation(peak)
                                                .apply(conf.quality_peaks)))
                            dict_list.append(dict_row)

                    full_df = None
                    sql_file_path = None
        df = pd.DataFrame(dict_list)
        df.to_csv(csv_path)

    @staticmethod
    def qualities_breaker_to_csv(csv_path='test_breaker.csv'):
        full_df = None
        dict_list = []
        sql_file_path = None
        for dirName, subdirList, fileList in os.walk(os.path.join(conf.dataset_path)):
            if 'YouTube' in dirName:
                sni = 'googlevideo'
            else:
                sni = 'nflxvideo'

            for fname in fileList:
                if fname.endswith('.csv'):
                    full_df = pd.read_csv(os.path.join(dirName, fname))
                elif fname.endswith('.mf'):
                    sql_file_path = os.path.join(dirName, fname)

                if full_df is not None and sql_file_path is not None:
                    divided_file_list = DataParser(df=full_df, sql_file=sql_file_path).divide_playbacks()
                    for one_playback in divided_file_list:
                        df = one_playback[data_frame]
                        qoe = one_playback[qualities]
                        sess_list = Interaction(df).get_sessions()
                        sess_sni_list = []
                        for sess in sess_list:
                            if sni in sess.get_sni():
                                sess_sni_list.append(sess.get_df())

                        df = pd.concat(sess_sni_list)
                        df.sort_values('frame.time_epoch')
                        req_res_list = [x for x in Breaker().get_dfs(df) if x['frame.len'].sum() > 3000]

                        curr_time = min(qoe)
                        curr_quality = qoe[curr_time]
                        del qoe[curr_time]
                        is_first = False
                        for req_res in req_res_list:
                            req_res_start_time = req_res['frame.time_epoch'].min()
                            req_res_end_time = req_res['frame.time_epoch'].max()
                            for time_key, quality in qoe.items():
                                if not (curr_time <= req_res_start_time and req_res_end_time <= time_key) and is_first:
                                    curr_time = time_key
                                    curr_quality = quality
                                    del qoe[curr_time]
                                    break

                            is_first = True
                            dict_row = {}
                            dict_row.update([('filter', "_"), ('source_file', fname),
                                             ('label', curr_quality), ('req_response_size', req_res['frame.len'].sum())])

                            dict_row.update(zip(conf.header_quality_breaker, FeaturesCalculation(req_res)
                                                .apply(conf.quality_breaker)))
                            dict_list.append(dict_row)

                    full_df = None
                    sql_file_path = None
        df = pd.DataFrame(dict_list)
        df.to_csv(csv_path)

    @staticmethod
    def qualities_bins_peaks_to_csv(csv_path='test_peaks_bins.csv', bin_size=1):
        full_df = None
        dict_list = []
        sql_file_path = None
        for dirName, subdirList, fileList in os.walk(os.path.join(conf.dataset_path)):
            if 'YouTube' in dirName:
                sni = 'googlevideo'
            else:
                sni = 'nflxvideo'

            for fname in fileList:
                if fname.endswith('.csv'):
                    full_df = pd.read_csv(os.path.join(dirName, fname))
                elif fname.endswith('.mf'):
                    sql_file_path = os.path.join(dirName, fname)

                if full_df is not None and sql_file_path is not None:
                    divided_file_list = DataParser(df=full_df, sql_file=sql_file_path).divide_playbacks()
                    for one_playback in divided_file_list:
                        df = one_playback[data_frame]
                        qoe = one_playback[qualities]
                        sess_list = Interaction(df).get_sessions()
                        bin_list = []

                        for sess in sess_list:
                            if sni in sess.get_sni():
                                peak_list = [x for x in Peaker(sess.get_df()).get_dfs() if x['frame.len'].sum() > 3000]
                                bin_list.extend(Peaker.get_bins(df_list=peak_list, bin_size=bin_size))
                        bin_list.sort(key=lambda x: (x[0]).iloc[0]['frame.time_epoch'])

                        first_time = min(qoe)
                        curr_quality = qoe[first_time]
                        del qoe[first_time]
                        not_first = False
                        for bin in bin_list:
                                max_bin_time = pd.concat(bin)['frame.time_epoch'].max()
                                min_bin_time = pd.concat(bin)['frame.time_epoch'].min()
                                for time_key, quality in qoe.items():
                                    if not(first_time <= min_bin_time and max_bin_time <= time_key) and not_first:
                                        first_time = time_key
                                        curr_quality = quality
                                        del qoe[first_time]
                                        break
                                not_first = True
                                if len(bin) != 0:
                                    dict = {}
                                    dict.update([('filter', ""), ('source_file', fname),
                                                 ('label', curr_quality)])
                                    dict.update(zip(conf.header_break,
                                                    FeatureAggregation(bin)
                                                    .apply(conf.app_agg)))
                                    dict.update(zip(conf.header_first,
                                                    FeaturesCalculation(bin[0])
                                                    .apply(conf.app_sess)))
                                    dict_list.append(dict)

                    full_df = None
                    sql_file_path = None
        df = pd.DataFrame(dict_list)
        df.to_csv(csv_path)

    @staticmethod
    def qualities_bins_breaker_to_csv(csv_path='test_breaker_bins.csv', bin_size=1):
        full_df = None
        dict_list = []
        sql_file_path = None
        for dirName, subdirList, fileList in os.walk(os.path.join(conf.dataset_path)):
            if 'YouTube' in dirName:
                sni = 'googlevideo'
            else:
                sni = 'nflxvideo'

            for fname in fileList:
                if fname.endswith('.csv'):
                    full_df = pd.read_csv(os.path.join(dirName, fname))
                elif fname.endswith('.mf'):
                    sql_file_path = os.path.join(dirName, fname)

                if full_df is not None and sql_file_path is not None:
                    divided_file_list = DataParser(df=full_df, sql_file=sql_file_path).divide_playbacks()
                    for one_playback in divided_file_list:
                        df = one_playback[data_frame]
                        qoe = one_playback[qualities]
                        sess_list = Interaction(df).get_sessions()
                        sess_sni_list = []
                        for sess in sess_list:
                            if sni in sess.get_sni():
                                sess_sni_list.append(sess.get_df())

                        df = pd.concat(sess_sni_list)
                        df.sort_values('frame.time_epoch')
                        req_res_list = [x for x in Breaker().get_dfs(df) if x['frame.len'].sum() > 3000]
                        bins_req_res_list = Breaker().get_bins(bin_size=bin_size, df_list=req_res_list)

                        first_time = min(qoe)
                        curr_quality = qoe[first_time]
                        del qoe[first_time]
                        not_first = False
                        for bin in bins_req_res_list:
                                max_bin_time = pd.concat(bin)['frame.time_epoch'].max()
                                min_bin_time = pd.concat(bin)['frame.time_epoch'].min()
                                for time_key, quality in qoe.items():
                                    if not(first_time <= min_bin_time and max_bin_time <= time_key) and not_first:
                                        first_time = time_key
                                        curr_quality = quality
                                        del qoe[first_time]
                                        break
                                not_first = True
                                if len(bin) != 0:
                                    dict = {}
                                    dict.update([('filter', ""), ('source_file', fname),
                                                 ('label', curr_quality)])
                                    dict.update(zip(conf.header_break,
                                                    FeatureAggregation(bin)
                                                    .apply(conf.app_agg)))
                                    dict.update(zip(conf.header_first,
                                                    FeaturesCalculation(bin[0])
                                                    .apply(conf.app_sess)))
                                    dict_list.append(dict)

                    full_df = None
                    sql_file_path = None
        df = pd.DataFrame(dict_list)
        df.to_csv(csv_path)

    @staticmethod
    def start_delay_bins_to_csv(peaker=False, breaker=False, bin_size=3, csv_path='test_delay_10.csv', x_seconds=10):
        full_df = None
        dict_list = []
        sql_file_path = None
        for dirName, subdirList, fileList in os.walk(os.path.join(conf.dataset_path)):
            if 'YouTube' in dirName:
                sni = 'googlevideo'
            else:
                sni = 'nflxvideo'

            for fname in fileList:
                if fname.endswith('.csv'):
                    full_df = pd.read_csv(os.path.join(dirName, fname))
                elif fname.endswith('.mf'):
                    sql_file_path = os.path.join(dirName, fname)

                if full_df is not None and sql_file_path is not None:
                    divided_file_list = DataParser(df=full_df, sql_file=sql_file_path).divide_playbacks()
                    for one_playback in divided_file_list:
                        df = one_playback[data_frame]
                        sess_list = Interaction(df).get_sessions()
                        start_delay_time = one_playback[delay_time]

                        for sess in sess_list:
                            if sni in sess.get_sni():
                                df = sess.get_df()
                                first_time = df['frame.time_epoch'].min()
                                df = df[(df['frame.time_epoch'] >= first_packet_time) & (df['frame.time_epoch'] <=
                                                                                         (first_time+x_seconds))]

                                if peaker:
                                    for bin in Peaker(df).get_bins(bin_size=bin_size):
                                        if len(bin) != 0:
                                            dict = {}
                                            dict.update([('filter', sess.to_filter()), ('source_file', fname),
                                                         ('label', start_delay_time), ('sni', sess.get_sni())])
                                            dict.update(zip(conf.header_break,
                                                            FeatureAggregation(bin)
                                                            .apply(conf.app_agg)))
                                            dict.update(zip(conf.header_first,
                                                            FeaturesCalculation(bin[0])
                                                            .apply(conf.app_sess)))
                                            dict_list.append(dict)

                                if breaker:
                                    for bin in Breaker().get_bins(df=df, bin_size=bin_size):
                                        if len(bin) != 0:
                                            dict = {}
                                            dict.update([('filter', sess.to_filter()), ('source_file', fname),
                                                         ('label', start_delay_time), ('sni', sess.get_sni())])
                                            dict.update(zip(conf.header_break,
                                                            FeatureAggregation(bin)
                                                            .apply(conf.app_agg)))
                                            dict.update(zip(conf.header_first,
                                                            FeaturesCalculation(bin[0])
                                                            .apply(conf.app_sess)))
                                            dict_list.append(dict)
                full_df = None
                sql_file_path = None

        df = pd.DataFrame(dict_list)
        df.to_csv(csv_path)


DataFactory.qualities_breaker_to_csv(csv_path='test2_breaker_filter3000_0.03_300.csv')
print("done1")
DataFactory.qualities_bins_peaks_to_csv(csv_path='test2_peaks_bins3_filter3000.csv', bin_size=3)
print("done2")

#DataFactory.qualities_big_packet_to_csv(breaker=True, csv_path='test_big_packet_breaker_0.03_250.csv')
#print("done3")

DataFactory.qualities_bins_breaker_to_csv(csv_path='test2_breaker_bins3_filter3000_0.03_300.csv', bin_size=3)
print("done4")

####
#DataFactory.start_delay_bins_to_csv(peaker=True, breaker=True)