import ast


class Label:

    @staticmethod
    def label_by_sni(sni_file_path, sni):
        with open(sni_file_path, 'r') as fp:
            file_cont = fp.read()
            dicts = ast.literal_eval(file_cont)
            for key, value in dicts.items():
                if key == sni:
                    return value
        return "None"

    @staticmethod
    def label_by_app(application):
        if application == "FaceBook":
            return 1
        elif application == "Netflix":
            return 2
        elif application == "YouTube":
            return 3
        elif application == "Other":
            return 4

    @staticmethod
    def label_by_video(video):
        if video == "video":
            return 0
        elif video == "Other":
            return 1
