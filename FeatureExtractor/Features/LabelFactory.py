import ast


class LabelFactory:

    @staticmethod
    def label_by_sni(dicts, sni):
        for key, value in dicts.items():
            for val in value:
                if val in sni:
                    return key
        return "None"

    @staticmethod
    def label_by_app(application):
        if application == "FaceBook":
            return 1
        elif application == "Netflix":
            return 2
        elif application == "YouTube":
            return 3
        elif application == "Instagram":
            return 4
        else:
            return 5

    @staticmethod
    def label_by_video(video):
        if video == "video":
            return 1
        else:
            return 2

    @staticmethod
    def label_by_video_video_like(video):
        if video == "video":
            return 1
        elif video == "video_like":
            return 2
        else:
            return 3
