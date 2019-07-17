import os
from configs.conf import *
from containers.Interaction import *
from features.FeaturesCalculation import *
from features.FeatureAggregation import *
from generators.datafactory import *
from tools.Breaker import *
from tools.Peaker import *
if __name__ == '__main__':
<<<<<<< HEAD:Src/Main.py
    # DataFactory.sessions_to_csv(breaker=True,path='sess_breaker.csv')
    # DataFactory.sessions_to_csv(peaker=True,path='sess_peaker')
    #DataFactory.make_csv()
=======
    DataFactory.sessions_to_csv(breaker=True,path='sess_breaker.csv')
    DataFactory.sessions_to_csv(peaker=True,path='sess_peaker')
>>>>>>> 2666c4218e22d9a8c75f2e89a8db89ee6d4a0f79:src/Main.py
    DataFactory.bins_to_csv(breaker=True,path='bins_breaker.csv')
    #DataFactory.bins_to_csv(peaker=True,path='bin_speaker.csv')
