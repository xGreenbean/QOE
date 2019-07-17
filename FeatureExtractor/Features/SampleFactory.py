from Features.Vector import Vector
from Generators.CsvGenerator import CsvGenerator
from Features.LabelFactory import LabelFactory
from Configs import conf
from Breaker import Breaker


class SampleFactory:

    @staticmethod
    def application_by_session(session, interval, dirName, with_first, is_skip):
        sni = session.get_sni()
        vector_session = Vector(session)
        vector_flow_up = Vector(session.flow_up)
        vector_flow_down = Vector(session.flow_down)
        vec_session = vector_session.get_vector_feature(conf.app_vid_session_features)
        # -- Flow up
        vec_flow_up_top = vector_flow_up.get_vector_feature_by_interval(interval, conf.app_vid_top_features, is_skip,
                                                                        with_first)
        vec_flow_up = vector_flow_up.get_vector_feature(conf.app_vid_flow_up_features)
        # -- Flow down
        vec_flow_down_top = vector_flow_down.get_vector_feature_by_interval(interval, conf.app_vid_top_features, is_skip,
                                                                            with_first)
        vec_flow_down = vector_flow_down.get_vector_feature(conf.app_vid_flow_down_features)

        all_vector = CsvGenerator.combine_list([vec_session, vec_flow_up_top, vec_flow_up, vec_flow_down_top,
                                                vec_flow_down])

        label = LabelFactory.label_by_sni(conf.application_sni, sni)
        if "netflix_download" in dirName:
            label = "Unknown"
        all_vector.append(LabelFactory.label_by_app(label))
        return all_vector

    @staticmethod
    def video_no_video_by_session(session, video_treshold, interval, dirName):
        sni = session.get_sni()
        session_size = session.get_session_size()
        vector_session = Vector(session)
        vector_flow_up = Vector(session.flow_up)
        vector_flow_down = Vector(session.flow_down)
        # -- Session
        vec_session = vector_session.get_vector_feature(conf.app_vid_session_features)
        # -- Flow up
        vec_flow_up_top = vector_flow_up.get_vector_feature_by_interval(interval, conf.app_vid_top_features)
        vec_flow_up = vector_flow_up.get_vector_feature(conf.app_vid_flow_up_features)
        # -- Flow down
        vec_flow_down_top = vector_flow_down.get_vector_feature_by_interval(interval, conf.app_vid_top_features)
        vec_flow_down = vector_flow_down.get_vector_feature(conf.app_vid_flow_down_features)

        all_vector = CsvGenerator.combine_list([vec_session, vec_flow_up_top, vec_flow_up, vec_flow_down_top,
                                                vec_flow_down])
        label = LabelFactory.label_by_sni(conf.video_no_video_sni, sni)
        if "netflix_download" in dirName or session_size < video_treshold:
            label = "Unknown"
        all_vector.append(LabelFactory.label_by_video(label))
        return all_vector

    @staticmethod
    def video_by_request_response_session(session, video_treshold, bin_size, delta_t, treshold,dirName):
        sni = session.get_sni()
        session_size = session.get_session_size()
        breaker = Breaker(session, delta_t, treshold)
        vector_request_response = Vector(breaker)
        vec_responses_requests = vector_request_response.get_vector_by_request_response_bins(bin_size, conf.response_request_top_features)

        label = LabelFactory.label_by_sni(conf.video_no_video_sni, sni)
        if "netflix_download" in dirName or session_size < video_treshold:
            label = "Unknown"
        for vector in vec_responses_requests:
            vector.append(LabelFactory.label_by_video(label))
        return vec_responses_requests

    @staticmethod
    def video_video_like_by_request_response_session(session, video_treshold, bin_size, delta_t, treshold, dirName):
        sni = session.get_sni()
        session_size = session.get_session_size()
        breaker = Breaker(session, delta_t, treshold)
        vector_request_response = Vector(breaker)
        vec_responses_requests = vector_request_response.get_vector_by_request_response_bins(bin_size,
                                                                                             conf.response_request_top_features)
        label = LabelFactory.label_by_sni(conf.video_videoLike_noVideo, sni)
        if label == "video" and session_size < video_treshold:
            label = "video_like"
        if "netflix_download" in dirName:
            label = "Unknown"
        for vector in vec_responses_requests:
            vector.append(LabelFactory.label_by_video_video_like(label))
        return vec_responses_requests

    @staticmethod
    def application_by_request_response_session(session, bin_size, delta_t, treshold, dirName):
        sni = session.get_sni()
        breaker = Breaker(session, delta_t, treshold)
        vector_request_response = Vector(breaker)
        vec_responses_requests = vector_request_response.get_vector_by_request_response_bins(bin_size,
                                                                                             conf.response_request_top_features)
        label = LabelFactory.label_by_sni(conf.application_sni, sni)
        if "netflix_download" in dirName:
            label = "Unknown"
        for vector in vec_responses_requests:
            vector.append(LabelFactory.label_by_app(label))
        return vec_responses_requests

    @staticmethod
    def app_rr_only(session, delta_t, treshold, dirName):
        sni = session.get_sni()
        breaker = Breaker(session, delta_t, treshold)
        vector_request_response = Vector(breaker)
        vec_responses_requests = vector_request_response.get_vector_by_request_response(conf.response_request_top_features)
        label = LabelFactory.label_by_sni(conf.application_sni, sni)
        if "netflix_download" in dirName:
            label = "Unknown"
        vec_responses_requests.append(LabelFactory.label_by_app(label))
        return vec_responses_requests

    @staticmethod
    def video_rr_only(session, delta_t, treshold, dirName):
        sni = session.get_sni()
        breaker = Breaker(session, delta_t, treshold)
        vector_request_response = Vector(breaker)
        vec_responses_requests = vector_request_response.get_vector_by_request_response(
            conf.response_request_top_features)
        label = LabelFactory.label_by_sni(conf.video_no_video_sni, sni)
        if "netflix_download" in dirName:
            label = "Unknown"
        vec_responses_requests.append(LabelFactory.label_by_video(label))
        return vec_responses_requests

    @staticmethod
    def app_peaks_only(session, interval, dirName, is_skip, with_first):
        sni = session.get_sni()
        vector = Vector(session)
        vec_peaks = vector.get_vector_feature_by_interval(interval, conf.app_vid_top_features, is_skip, with_first)
        label = LabelFactory.label_by_sni(conf.application_sni, sni)
        if "netflix_download" in dirName:
            label = "Unknown"
        vec_peaks.append(LabelFactory.label_by_app(label))
        return vec_peaks

    @staticmethod
    def video_peaks_only(session,interval, dirName, is_skip, with_first):
        sni = session.get_sni()
        vector = Vector(session)
        vec_peaks = vector.get_vector_feature_by_interval(interval, conf.app_vid_top_features, is_skip, with_first)
        label = LabelFactory.label_by_sni(conf.video_no_video_sni, sni)
        if "netflix_download" in dirName:
            label = "Unknown"
        vec_peaks.append(LabelFactory.label_by_video(label))
        return vec_peaks


    @staticmethod
    def session_headers(with_first):
        session_headers = CsvGenerator.custom_headers(conf.app_vid_session_features, "session")
        if with_first:
            flow_up_top_headers = CsvGenerator.custom_headers(conf.app_vid_top_features, "flow_up")
            flow_down_top_headers = CsvGenerator.custom_headers(conf.app_vid_top_features, "flow_down")
        else:
            flow_up_top_headers = CsvGenerator.custom_headers(conf.app_vid_top_features[:-1], "flow_up")
            flow_down_top_headers = CsvGenerator.custom_headers(conf.app_vid_top_features[:-1], "flow_down")
        flow_up_headers = CsvGenerator.custom_headers(conf.app_vid_flow_up_features, "flow_up")
        flow_down_headers = CsvGenerator.custom_headers(conf.app_vid_flow_down_features, "flow_down")
        headers = CsvGenerator.combine_list([session_headers, flow_up_top_headers, flow_up_headers,
                                             flow_down_top_headers, flow_down_headers])
        headers.append("Label")
        return headers

    @staticmethod
    def session_request_response_headers():
        request_response_headers = CsvGenerator.custom_headers(conf.response_request_top_features, "rr")
        request_response_headers.append("Label")
        return request_response_headers

    @staticmethod
    def session_peaks_headers(with_first):
        if with_first:
            request_response_headers = CsvGenerator.custom_headers(conf.app_vid_top_features, "rr")
        else:
            request_response_headers = CsvGenerator.custom_headers(conf.app_vid_top_features[:-1], "rr")
        request_response_headers.append("Label")
        return request_response_headers
