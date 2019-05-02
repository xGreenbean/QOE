import pandas as pd

# "Address A" "Address B" "Port A" "Port B"
video_real = pd.read_csv('sni.csv')

video_predicted = pd.read_csv('predicted.csv')

for _i in range(video_predicted.shape[0]):
    video_predicted.values[_i][2] = (video_predicted.values[_i][2].replace('"', "")).replace(' ', "")

for _j in range(video_real.shape[0]):
    video_real.values[_j][2] = (video_real.values[_j][2].replace('"', "")).replace(' ', "")

for _i in range(video_predicted.shape[0]):
    for _j in range(video_real.shape[0]):
        if (video_real.values[_j][0] == video_predicted.values[_i][0]) and \
                (video_real.values[_j][1] == video_predicted.values[_i][1]) and \
                (video_predicted.values[_i][2].replace('"', "")).replace(' ', "") == \
                (video_real.values[_j][2].replace('"', "")).replace(' ', "") and \
                (video_real.values[_j][3] == video_predicted.values[_i][3]):
            print(video_real.values[_j])
