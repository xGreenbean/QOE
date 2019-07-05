import os
from configs.conf import *
from containers.Interaction import *
from features.FeaturesCalculation import *
from features.FeatureAggregation import *

from tools.Breaker import *
from tools.Peaker import *
if __name__ == '__main__':
    df = pd.read_csv(os.path.join(dataset_path,'Iphone_youtube/id_4/raw_iphone7_auto_04_19_id_4.csv'))
    test = Interaction(df)
    for sess in test.get_sessions():
        print(sess.get_label(video))
