from Configs import conf


class Label:

    def __init__(self):
        self.isVideo = False
        self.isVideoLike = False
        self.ott = ""
        self.isDownload = False

    @staticmethod
    def set_ott_from_sni(sni):
        for key, value in conf.application_sni.iteritems():
            for val in value:
                if sni.contains(val):
                    return key
        return "None"

    def set_video_from_sni(sni):
        for key, value in conf.application_sni.iteritems():
            for val in value:
                if sni.contains(val):
                    return key
        return "None"

    def set_video_from_sni(sni):
        for key, value in conf.application_sni.iteritems():
            for val in value:
                if sni.contains(val):
                    return key
        return "None"
