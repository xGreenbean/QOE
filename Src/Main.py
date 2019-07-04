import os
from configs.conf import *
from containers.Interaction import *
from features.FeaturesCalculation import *

from tools.Peaker import *
if __name__ == '__main__':
    df = pd.read_csv(os.path.join(dataset_path,'Iphone_facebook/id_1/raw_iphone7_facebook_04_19_id_1.csv'))
    test = Interaction(df)
    for sess in test.get_sessions():
        fc = FeaturesCalculation(sess.df)
        print(fc.apply(app_sess))