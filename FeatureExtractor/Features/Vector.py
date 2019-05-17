from Features.FeaturesCalculation import FeaturesCalculation
from Features.TopFeatures import TopFeatures


class Vector:

    def __init__(self, pc, name):
        self.pc = pc
        self.name = name
    def get_vector_by_request_response(self, bin_size):
        pass

    def get_vector_by_streamer(self):
        pass

    def get_vector_feature(self, fc_l):
        df = self.pc.getSample()
        fc = FeaturesCalculation(df)
        for feature in fc_l:
            method = getattr(fc, feature)
            print(self.name + "_" +feature + "         " + str(method()))

    def get_vector_feature_by_interval(self, interval, ft_l):
        ft = TopFeatures(self.pc.split(interval))
        for feature in ft_l:
            method = getattr(ft, feature)
            print(feature + "         " + str(method()))
