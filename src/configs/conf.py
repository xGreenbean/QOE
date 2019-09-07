# ----------------------------------------------------------  SNI configs ------------------------------------------
"""
SNI dictionaries in order to decide which labels to give either to app features set or video/non video set(Both get
 "Other" as thresh for unrecognized sessions)
"""
application_sni = {
    "Netflix": ["nflxvideo"],
    "FaceBook": ["fbcdn", "graph"],
    "YouTube": ["googlevideo"],
    "Instagram": ["cdninstagram"],
    "OtherOTT": ["video.twimg.com", "cnnios-f.akamaihd.net"],
    "unknown": []
}

video = {
    "video": ["nflxvideo", "fbcdn", "googlevideo", "cdninstagram", "cnnios-f.akamaihd.net", "video.twimg.com"],
    "unknown": []
}

videolike = {
    "video": ["nflxvideo", "fbcdn", "googlevideo","cdninstagram", "cnnios-f.akamaihd.net", "video.twimg.com"],
    "video_like": [],
    "unknown": []
}

quality_dict = {
    ' 1280x720': 1,
    ' 864x480': 2,
    ' 640x368': 3,
    ' 1920x1088': 4,
}

delay_range = {"1-2": '1', "2-3": '2', "3-4": '3', "4-5": '4', "5-8": '5'}

"""path to dataset"""

dataset_path = 'C:\\Users\\Saimon\\Desktop\\idk\\dataset'

# ------------------------------------------------------------------------------------------------------------------
"""Breaker settings"""
delta_t = 0.03
threshold_t = 250

# ---------------------------------- Video/non and Application features for classification  -------------------------

"""app_vid - Feature lists to build the vector for video / no video and 
   application by session(size histogram and extension misses),
   ##### These only for TCP session. For udp All tcp&ssl features from flow up need to be gone.  """

app_agg = ["max_element_size", "min_element_size", "mean_element_size", "std_element_size", "var_element_size",
           "sum_element_size", "max_silence_time", "min_silence_time","mean_silence_time", "std_silence_time",
            "var_silence_time", "sum_silence_time",
           "element_count", "max_element_length",
           "min_element_length", "std_element_length", "mean_element_length", "var_element_length", "sum_element_length",
           "max_element_time", "min_element_time", "mean_element_time", "std_element_time", "var_element_time", "sum_element_time"]

app_sess = ["packet_count", "min_packet_size", "max_packet_size",
                            "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                            "min_time_delta", "mean_time_delta", "duration", "packets_size", "upstream_mean_ttl",
                   "size_histogram"]

app_flowup = ["upstream_cipher_suites", "upstream_ssl_v", "upstream_ssl_session_id_len",
                            "upstream_ssl_num_compression_methods", "packet_count", "min_packet_size",
                            "max_packet_size", "mean_packet_size", "std_packet_size", "size_var", "syn_tcp_scale",
                            "syn_mss", "syn_tcp_win_size", "max_time_delta", "std_time_delta", "min_time_delta",
                            "mean_time_delta", "upstream_mean_ttl", "upstream_num_keep_alive"]

app_flowdown = ["packet_count", "min_packet_size", "max_packet_size",
                              "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                              "min_time_delta", "mean_time_delta"]

network_features = ["packet_count", "min_packet_size", "max_packet_size",
                              "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                              "min_time_delta", "var_time_delta", "mean_time_delta", "duration", "packets_size", "upstream_mean_ttl",
                   "size_histogram"]

net_tran_features = ["packet_count", "min_packet_size", "max_packet_size",
                              "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                              "min_time_delta", "var_time_delta", "mean_time_delta", "duration", "packets_size", "upstream_mean_ttl",
                   "size_histogram", "tran_len_sum", "tran_len_max", "tran_len_min", "tran_len_mean", "tran_len_std", "tran_len_var",
                     "tran_time_relative_sum", "tran_time_relative_max", "tran_time_relative_min",
                     "tran_time_relative_mean", "tran_time_relative_std", "tran_time_relative_var",
                    "tran_time_delta_sum", "tran_time_delta_max", "tran_time_delta_min",
                    "tran_time_delta_mean", "tran_time_delta_std", "tran_time_delta_var"]



# ------------------------------------------------------------------------------------------------------------------
#Headers..

header_first = ["f_packet_count", "f_min_packet_size", "f_max_packet_size",
                "f_mean_packet_size", "f_std_packet_size", "f_size_var", "f_max_time_delta",
                "f_std_time_delta", "f_min_time_delta", "f_mean_time_delta", "f_duration", "f_packets_size", "f_upstream_mean_ttl",
                   "f_size_histogram"]

header_network = ["packet_count", "min_packet_size", "max_packet_size",
                              "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                              "min_time_delta", "var_time_delta", "mean_time_delta", "duration", "packets_size", "upstream_mean_ttl",
                   "size_histogram"]

header_transport = ["tran_len_sum", "tran_len_max", "tran_len_min", "tran_len_mean", "tran_len_std", "tran_len_var",
                     "tran_time_relative_sum", "tran_time_relative_max", "tran_time_relative_min",
                     "tran_time_relative_mean", "tran_time_relative_std", "tran_time_relative_var",
                    "tran_time_delta_sum", "tran_time_delta_max", "tran_time_delta_min",
                    "tran_time_delta_mean", "tran_time_delta_std", "tran_time_delta_var"]

header_net_tran_up = ["up_packet_count", "up_min_packet_size", "up_max_packet_size",
                              "up_mean_packet_size", "up_std_packet_size", "up_size_var", "up_max_time_delta", "up_std_time_delta",
                              "up_min_time_delta", "up_var_time_delta", "up_mean_time_delta", "up_duration", "up_packets_size", "up_upstream_mean_ttl",
                   "up_size_histogram", "up_tran_len_sum", "up_tran_len_max", "up_tran_len_min", "up_tran_len_mean", "up_tran_len_std", "up_tran_len_var",
                     "up_tran_time_relative_sum", "up_tran_time_relative_max", "up_tran_time_relative_min",
                     "up_tran_time_relative_mean", "up_tran_time_relative_std", "up_tran_time_relative_var",
                    "up_tran_time_delta_sum", "up_tran_time_delta_max", "up_tran_time_delta_min",
                    "up_tran_time_delta_mean", "up_tran_time_delta_std", "up_tran_time_delta_var"]

header_net_tran_down = ["d_packet_count", "d_min_packet_size", "d_max_packet_size",
                              "d_mean_packet_size", "d_std_packet_size", "d_size_var", "d_max_time_delta", "d_std_time_delta",
                              "d_min_time_delta", "d_var_time_delta", "d_mean_time_delta", "duration", "d_packets_size", "d_upstream_mean_ttl",
                   "d_size_histogram", "d_tran_len_sum", "d_tran_len_max", "d_tran_len_min", "d_tran_len_mean", "d_tran_len_std", "d_tran_len_var",
                     "d_tran_time_relative_sum", "d_tran_time_relative_max", "d_tran_time_relative_min",
                     "d_tran_time_relative_mean", "d_tran_time_relative_std", "d_tran_time_relative_var",
                    "d_tran_time_delta_sum", "d_tran_time_delta_max", "d_tran_time_delta_min",
                    "d_tran_time_delta_mean", "d_tran_time_delta_std", "d_tran_time_delta_var"]

header_net_tran = ["packet_count", "min_packet_size", "max_packet_size",
                              "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                              "min_time_delta", "var_time_delta", "mean_time_delta", "duration", "packets_size", "upstream_mean_ttl",
                   "size_histogram", "tran_len_sum", "tran_len_max", "tran_len_min", "tran_len_mean", "tran_len_std", "tran_len_var",
                     "tran_time_relative_sum", "tran_time_relative_max", "tran_time_relative_min",
                     "tran_time_relative_mean", "tran_time_relative_std", "tran_time_relative_var",
                    "tran_time_delta_sum", "tran_time_delta_max", "tran_time_delta_min",
                    "tran_time_delta_mean", "tran_time_delta_std", "tran_time_delta_var"]



header_peak = ["p_max_element_size", "p_min_element_size", "p_mean_element_size",
                 "p_std_element_size",  "p_var_element_size", "p_sum_element_size", "p_max_silence_time",
           "p_min_silence_time","p_mean_silence_time", "p_std_silence_time", "p_var_silence_time", "p_sum_silence_time",
                 "p_element_count", "p_max_element_length",
           "p_min_element_length", "p_std_element_length", "p_mean_element_length", "p_var_element_length",
                "p_sum_element_length", "p_max_element_time", "p_min_element_time", "p_mean_element_time",
                "p_std_element_time", "p_var_element_time", "p_sum_element_time"]

header_break = ["b_max_element_size", "b_min_element_size", "b_mean_element_size",
                 "b_std_element_size", "b_var_element_size", "b_sum_element_size", "b_max_silence_time",
                "b_min_silence_time","b_mean_silence_time", "b_std_silence_time", "b_var_silence_time", "b_sum_silence_time"
                 "b_element_count", "b_max_element_length",
           "b_min_element_length", "b_std_element_length", "b_mean_element_length", "b_var_element_length",
                "b_sum_element_length",  "b_max_element_time", "b_min_element_time", "b_mean_element_time",
                "b_std_element_time", "b_var_element_time", "b_sum_element_time"]

header_big_pakcet = ["bp_max_element_size", "bp_min_element_size", "bp_mean_element_size",
                 "bp_std_element_size", "bp_var_element_size", "bp_sum_element_size", "bp_max_silence_time",
                "bp_min_silence_time","bp_mean_silence_time", "bp_std_silence_time", "bp_var_silence_time", "bp_sum_silence_time"
                 "bp_element_count", "bp_max_element_length",
           "bp_min_element_length", "bp_std_element_length", "bp_mean_element_length", "bp_var_element_length",
                "bp_sum_element_length",  "bp_max_element_time", "bp_min_element_time", "bp_mean_element_time",
                "bp_std_element_time", "bp_var_element_time", "bp_sum_element_time"]

header_sess = ["s_packet_count", "s_min_packet_size", "s_max_packet_size", "s_mean_packet_size", "s_std_packet_size",
               "s_size_var", "s_max_time_delta", "s_std_time_delta", "s_min_time_delta", "s_mean_time_delta",
               "s_duration", "s_packets_size", "s_upstream_mean_ttl", "size_histogram"]

header_up = ["upstream_cipher_suites", "upstream_ssl_v", "upstream_ssl_session_id_len",
               "upstream_ssl_num_compression_methods", "u_packet_count", "u_min_packet_size", "u_max_packet_size",
               "u_mean_packet_size", "u_std_packet_size", "u_size_var", "syn_tcp_scale",  "syn_mss", "syn_tcp_win_size",
               "u_max_time_delta", "u_std_time_delta", "u_min_time_delta" "u_mean_time_delta", "upstream_mean_ttl", "upstream_num_keep_alive"]

header_down = ["d_packet_count", "d_min_packet_size", "d_max_packet_size", "d_mean_packet_size", "d_std_packet_size",
               "d_size_var", "d_max_time_delta", "d_std_time_delta", "d_min_time_delta", "d_mean_time_delta"]

header_streamer = ["sni", "verdict", "enc", "duration", "vol", "rate", "avg pkt len", "type", 'tcp/udp']