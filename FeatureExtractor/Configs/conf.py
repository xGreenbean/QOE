# ----------------------------------------------------------  SNI configs ------------------------------------------
"""
SNI dictionaries in order to decide which labels to give either to app features set or video/non video set(Both get
 "Other" as thresh for unrecognized sessions)
"""
application_sni = {
    "Netflix": ["netflix", "nflxvideo", "nflxso", "nflx", ],
    "FaceBook": ["facebook", "fbcdn"],
    "YouTube": ["googlevideo", "youtube", "Youtube", "YouTube", "ads", "yt"]
}

video_no_video_sni = {
    "video": ["netflix", "nflxvideo", "nflxso", "nflx", "facebook", "fbcdn", "googlevideo"]
}

""" 
   SNI dictionaries for {SNI:VIDEO,SNI:OTHER} convert by Label class to {sni:0,sni:1} - "sni_video_other.txt"
    and {SNI:FaceBook,SNI:Netfilx,SNI:YouTube,SNI:Other} converting to {sni:1,sni:2,sni:3,sni:4} - "sni_application.txt"
"""

sni_to_read = "sni_video_other.txt"

# ------------------------------------------------------------------------------------------------------------------

# ----------------------------------- Parameters for  Data factory iterators ---------------------------------------

Otts = ["YouTube", "Netflix", "FaceBook"]
Devices = ["onePlus6", "iphone7"]
numbers_of_id = 5

"""
    Reading data set for features need to include video or app string to decide which features to get 
"""
feature_type = "video"

# ---------------------------------- Video/non and Application features for classification  -------------------------

"""app_vid - Feature lists to build the vector for video / no video and 
   application by session(size histogram and extension misses),
   ##### These only for TCP session. For udp All tcp&ssl features from flow up need to be gone.  """
app_vid_top_features = ["max_peak", "min_peak", "std_peak", "mean_peak", "max_silence_time", "min_silence_time",
                        "mean_silence_time", "std_silence_time", "peaks_count"]

app_vid_session_features = ["packet_count", "min_packet_size", "max_packet_size",
                            "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                            "min_time_delta", "mean_time_delta"]

app_vid_flow_up_features = ["upstream_cipher_suites", "upstream_ssl_v", "upstream_ssl_session_id_len",
                            "upstream_ssl_num_compression_methods", "packet_count", "min_packet_size",
                            "max_packet_size", "mean_packet_size", "std_packet_size", "size_var", "syn_tcp_scale",
                            "syn_mss", "syn_tcp_win_size", "max_time_delta", "std_time_delta", "min_time_delta",
                            "mean_time_delta", "upstream_mean_ttl", "upstream_num_keep_alive"]

app_vid_flow_down_features = ["packet_count", "min_packet_size", "max_packet_size",
                              "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                              "min_time_delta", "mean_time_delta"]
# ------------------------------------------------------------------------------------------------------------------
