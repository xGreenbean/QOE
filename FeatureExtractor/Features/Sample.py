from Features.Vector import Vector


class Sample:

    """app_vid - Feature lists to build the vector for video / novideo and application by session"""
    app_vid_top_features = ["max_peak", "min_peak", "std_peak", "mean_peak", "max_silence_time", "min_silence_time",
                            "mean_silence_time", "std_silence_time", "peaks_count"]

    app_vid_session_features = ["size_histogram", "packet_count", "min_packet_size", "max_packet_size",
                                "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                                "min_time_delta", "mean_time_delta"]

    app_vid_flow_up_features = ["upstream_cipher_suites", "upstream_ssl_v", "upstream_ssl_session_id_len",
                                "upstream_ssl_num_extensions",
                                "upstream_ssl_num_compression_methods", "size_histogram", "packet_count",
                                "min_packet_size",
                                "max_packet_size", "mean_packet_size", "std_packet_size", "size_var", "syn_tcp_scale",
                                "syn_mss", "syn_tcp_win_size", "max_time_delta", "std_time_delta", "min_time_delta",
                                "mean_time_delta", "upstream_mean_ttl",
                                "upstream_num_keep_alive"]

    app_vid_flow_down_features = ["size_histogram", "packet_count", "min_packet_size", "max_packet_size",
                                  "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                                  "min_time_delta", "mean_time_delta"]

    @staticmethod
    def video_no_video_by_session(session, interval):
        vector_session = Vector(session, "Session")
        vector_flow_up = Vector(session.flow_up, "Flow_up")
        vector_flow_down = Vector(session.flow_down, "Flow_down")
        # -- Session
        vector_session.get_vector_feature(Sample.app_vid_session_features)
        # -- Flow up
        vector_flow_up.get_vector_feature_by_interval(interval, Sample.app_vid_top_features)
        vector_flow_up.get_vector_feature(Sample.app_vid_flow_up_features)
        # -- Flow down
        vector_flow_down.get_vector_feature_by_interval(interval, Sample.app_vid_top_features)
        vector_flow_down.get_vector_feature(Sample.app_vid_flow_down_features)
