from Features.FeaturesCalculation import FeaturesCalculation
from Features.TopFeatures import TopFeatures


class Vector:

    def __init__(self, pc):
        self.pc = pc

    def get_vector_by_request_response(self, ft_l):
        array_df = self.pc.getSample()
        fc = TopFeatures(array_df)
        results = []
        for feature in ft_l:
            method = getattr(fc, feature)
            results.append(str(method()))
        return results

    def get_vector_by_request_response_bins(self, bin_size, ft_l):
        array_df = self.pc.split(bin_size)
        fc = TopFeatures(array_df)
        results = []
        for feature in ft_l:
            method = getattr(fc, feature)
            results.append(str(method()))
        return results

    def get_vector_by_streamer(self):
        pass

    def get_vector_feature(self, fc_l):
        df = self.pc.getSample()
        fc = FeaturesCalculation(df)
        results = []
        for feature in fc_l:
            method = getattr(fc, feature)
            results.append(str(method()))
        return results

    def get_vector_feature_by_interval(self, interval, ft_l):
        ft = TopFeatures(self.pc.split(interval))
        results = []
        for feature in ft_l:
            method = getattr(ft, feature)
            results.append(method())
        return results
