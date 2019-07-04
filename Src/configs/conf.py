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
    "OtherOTT": ["video.twimg.com", "cnnios-f.akamaihd.net"]
}

video = {
    "video": ["nflxvideo", "fbcdn", "googlevideo", "cdnistagram", "cnnios-f.akamaihd.net", "video.twimg.com"]
}

videolike = {
    "video": ["nflxvideo", "fbcdn", "googlevideo","cdnistagram", "cnnios-f.akamaihd.net", "video.twimg.com"],
    "video_like": []
}




"""path to dataset"""
dataset_path = '/home/ehud/Desktop/dataset'
# ------------------------------------------------------------------------------------------------------------------




# ---------------------------------- Video/non and Application features for classification  -------------------------

"""app_vid - Feature lists to build the vector for video / no video and 
   application by session(size histogram and extension misses),
   ##### These only for TCP session. For udp All tcp&ssl features from flow up need to be gone.  """
app_top = ["max_peak", "min_peak", "std_peak", "mean_peak", "max_silence_time", "min_silence_time",
                        "mean_silence_time", "std_silence_time", "peaks_count",
                        "max_peak_length", "min_peak_length", "std_peak_length", "mean_peak_length", "first_peak"]

app_agg = ["max_element_size", "min_element_size", "mean_element_size", "std_element_size", ]

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

act_top = ["max_response_request", "min_response_request", "std_response_request",
                                                 "mean_response_request", "max_response_request",
                                                 "min_response_request_delta_time", "max_response_request_delta_time",
                                                 "std_response_request_delta_time", "mean_response_request_delta_time",
                                                "max_request_response_length","min_request_response_length",
                                                "mean_request_response_length", "std_request_response_length",
                                 "request_response_count"]

first_peak = ["packets_size", "packet_count", "min_packet_size", "max_packet_size",
                            "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                            "min_time_delta", "mean_time_delta"]

# ------------------------------------------------------------------------------------------------------------------
