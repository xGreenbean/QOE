import os
from configs.conf import *
from containers.Interaction import *
from features.FeaturesCalculation import *
from features.FeatureAggregation import *
from generators.datafactory import *
from tools.Breaker import *
from tools.Peaker import *
if __name__ == '__main__':
    DataFactory.sessions_to_csv(breaker=True,path='sess_breaker.csv')
    DataFactory.sessions_to_csv(peaker=True,path='sess_peaker')
    DataFactory.bins_to_csv(breaker=True,path='bins_breaker.csv')
    DataFactory.bins_to_csv(peaker=True,path='bin_speaker.csv')
