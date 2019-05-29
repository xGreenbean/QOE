from Features.Vector import Vector
from Generators.CsvGenerator import CsvGenerator
from Features.LabelFactory import Label
from Configs import conf
from Breaker import Breaker


class SampleFactory:

    @staticmethod
    def application_by_session(session, sni_file_name, interval):
        sni = session.get_sni()
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
        label = Label.label_by_sni(sni_file_name, sni)
        all_vector.append(Label.label_by_app(label))
        return all_vector

    @staticmethod
    def video_no_video_by_session(session, sni_file_name, interval):
        sni = session.get_sni()
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
        label = Label.label_by_sni(sni_file_name, sni)
        all_vector.append(Label.label_by_video(label))
        return all_vector

    @staticmethod
    def video_by_request_response_session(session, sni_file_name, bin_size, delta_t, treshold):
        sni = session.get_sni()
        breaker = Breaker(session, delta_t, treshold)
        vector_request_response = Vector(breaker)
        vec_responses_requests = vector_request_response.get_vector_by_request_response_bins(bin_size, conf.video_non_video_response_request_top_features)
        label = Label.label_by_sni(sni_file_name, sni)
        for vector in vec_responses_requests:
            vector.append(Label.label_by_video(label))
        return vec_responses_requests

    @staticmethod
    def app_by_request_response_session(session, sni_file_name, bin_size, delta_t, treshold):
        sni = session.get_sni()
        breaker = Breaker(session, delta_t, treshold)
        vector_request_response = Vector(breaker)
        vec_responses_requests = vector_request_response.get_vector_by_request_response_bins(bin_size,
                                                                                             conf.app_vid_top_features)
        label = Label.label_by_sni(sni_file_name, sni)
        for vector in vec_responses_requests:
            vector.append(Label.label_by_app(label))
        return vec_responses_requests

    @staticmethod
    def video_no_video_by_session_headers():
        session_headers = CsvGenerator.custom_headers(conf.app_vid_session_features, "session")
        flow_up_top_headers = CsvGenerator.custom_headers(conf.app_vid_top_features, "flow_up")
        flow_up_headers = CsvGenerator.custom_headers(conf.app_vid_flow_up_features, "flow_up")
        flow_down_top_headers = CsvGenerator.custom_headers(conf.app_vid_top_features, "flow_down")
        flow_down_headers = CsvGenerator.custom_headers(conf.app_vid_flow_down_features, "flow_down")
        headers = CsvGenerator.combine_list([session_headers, flow_up_top_headers, flow_up_headers,
                                             flow_down_top_headers, flow_down_headers])
        headers.append("Label")
        return headers

    @staticmethod
    def app_session_headers():
        session_headers = CsvGenerator.custom_headers(conf.app_vid_session_features, "session")
        flow_up_top_headers = CsvGenerator.custom_headers(conf.app_vid_top_features, "flow_up")
        flow_up_headers = CsvGenerator.custom_headers(conf.app_vid_flow_up_features, "flow_up")
        flow_down_top_headers = CsvGenerator.custom_headers(conf.app_vid_top_features, "flow_down")
        flow_down_headers = CsvGenerator.custom_headers(conf.app_vid_flow_down_features, "flow_down")
        headers = CsvGenerator.combine_list([session_headers, flow_up_top_headers, flow_up_headers,
                                             flow_down_top_headers, flow_down_headers])
        headers.append("Label")
        return headers

    @staticmethod
    def video_session_request_response_headers():
        request_response_headers = CsvGenerator.custom_headers(conf.app_vid_top_features, "rr")
        request_response_headers.append("Label")
        return request_response_headers
