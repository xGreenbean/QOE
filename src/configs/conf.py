# ----------------------------------------------------------  SNI configs ------------------------------------------
"""
SNI dictionaries in order to decide which labels to give either to app features set or video/non video set(Both get
 "Other" as thresh for unrecognized sessions)
"""
application_sni = {
    "Netflix": ["nflxvideo"],
    "FaceBook": ["fbcdn", "graph"],
    "YouTube": ["googlevideo"],
    "Instagram": ["cdnistagram"],
    "OtherOTT": ["video.twimg.com", "cnnios-f.akamaihd.net"],
    "unknown":[]
}

video = {
    "video": ["nflxvideo", "fbcdn", "googlevideo", "cdnistagram", "cnnios-f.akamaihd.net", "video.twimg.com"],
    "unknown":[]
}

videolike = {
    "video": ["nflxvideo", "fbcdn", "googlevideo","cdnistagram", "cnnios-f.akamaihd.net", "video.twimg.com"],
    "video_like": [],
    "unknown":[]
}




"""path to dataset"""
dataset_path = '/home/ehud/Desktop/dataset'
# ------------------------------------------------------------------------------------------------------------------
"""Breaker settings"""
delta_t = 0.1
threshold_t = 400

# ---------------------------------- Video/non and Application features for classification  -------------------------

"""app_vid - Feature lists to build the vector for video / no video and 
   application by session(size histogram and extension misses),
   ##### These only for TCP session. For udp All tcp&ssl features from flow up need to be gone.  """

app_agg = ["max_element_size", "min_element_size", "mean_element_size", "std_element_size","max_silence_time",
           "min_silence_time","mean_silence_time", "std_silence_time", "element_count", "max_element_length",
           "min_element_length", "std_element_length", "mean_element_length"]

app_sess = ["packet_count", "min_packet_size", "max_packet_size",
                            "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                            "min_time_delta", "mean_time_delta"]

app_flowup = ["upstream_cipher_suites", "upstream_ssl_v", "upstream_ssl_session_id_len",
                            "upstream_ssl_num_compression_methods", "packet_count", "min_packet_size",
                            "max_packet_size", "mean_packet_size", "std_packet_size", "size_var", "syn_tcp_scale",
                            "syn_mss", "syn_tcp_win_size", "max_time_delta", "std_time_delta", "min_time_delta",
                            "mean_time_delta", "upstream_mean_ttl", "upstream_num_keep_alive"]

app_flowdown = ["packet_count", "min_packet_size", "max_packet_size",
                              "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                              "min_time_delta", "mean_time_delta"]

# ------------------------------------------------------------------------------------------------------------------
#Headers..
header_first = ["f_packet_count", "f_min_packet_size", "f_max_packet_size",
                            "f_mean_packet_size", "f_std_packet_size", "f_size_var", "f_max_time_delta", "f_std_time_delta",
                            "f_min_time_delta", "f_mean_time_delta"]

header_peak = ["p_max_element_size", "p_min_element_size", "p_mean_element_size",
                 "p_std_element_size","p_max_silence_time",
           "p_min_silence_time","p_mean_silence_time", "p_std_silence_time",
                 "p_element_count", "p_max_element_length",
           "p_min_element_length", "p_std_element_length", "p_mean_element_length"]

header_break = ["b_max_element_size", "b_min_element_size", "b_mean_element_size",
                 "b_std_element_size","b_max_silence_time",
           "b_min_silence_time","b_mean_silence_time", "b_std_silence_time",
                 "b_element_count", "b_max_element_length",
           "b_min_element_length", "b_std_element_length", "b_mean_element_length"]

header_sess = ["s_packet_count", "s_min_packet_size", "s_max_packet_size",
                            "s_mean_packet_size", "s_std_packet_size",
              "s_size_var", "s_max_time_delta", "s_std_time_delta",
                            "s_min_time_delta", "s_mean_time_delta"]

header_down = ["upstream_cipher_suites", "upstream_ssl_v", "upstream_ssl_session_id_len",
                            "upstream_ssl_num_compression_methods", "u_packet_count", "u_min_packet_size",
                            "u_max_packet_size", "u_mean_packet_size", "u_std_packet_size", "u_size_var", "syn_tcp_scale",
                            "syn_mss", "syn_tcp_win_size", "u_max_time_delta", "u_std_time_delta", "u_min_time_delta",
                            "u_mean_time_delta", "upstream_mean_ttl", "upstream_num_keep_alive"]

header_up = ["d_packet_count", "d_min_packet_size", "d_max_packet_size",
                              "d_mean_packet_size", "d_std_packet_size", "d_size_var", "d_max_time_delta",
               "d_std_time_delta",
                              "d_min_time_delta", "d_mean_time_delta"]
header_streamer = ["sni", "verdict", "enc", "duration", "vol", "rate", "avg pkt len", "type", 'tcp/udp']