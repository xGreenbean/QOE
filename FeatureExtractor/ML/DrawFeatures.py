from Configs import conf
import pandas as pd


def draw_features():
    frames = []
    for device in conf.Devices:
        for ott in conf.Otts:
            if ott != "download" and device != "onePlus6":
                for i in range(conf.numbers_of_id):
                    df = pd.read_csv(
                        "C:\\Users\\Saimon\\Desktop\\dataset\\" + device + "_" + ott + "\\Id_" + str(
                            i + 1) + "\\" + device + "_" + ott + "_"+conf.feature_type+"request_response_features_" + str(
                            i + 1) + ".csv")
                    frames.append(df)
    print("Done Reading")
    result = pd.concat(frames)
    return result
