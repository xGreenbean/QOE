import os
from configs.conf import *
from containers.Interaction import *
from tools.Streamer import *
if __name__ == '__main__':
    df = pd.read_csv(os.path.join(dataset_path,'Iphone_youtube/id_4/iphone7_auto_04_19_id_4.csv'))
    test = Interaction(df)
    s = Streamer(test, 5, 0.1, 50000)
    print(len(s.get_video_related_sessions()))