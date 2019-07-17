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
            results.append(method())
        return results

    def get_vector_by_request_response_bins(self, bin_size, ft_l):
        array_df = self.pc.split(bin_size)
        all_results = []
        for bin_df in array_df:
            if not bin_df.empty:
                fc = TopFeatures(bin_df)
                bin_result = []
                for feature in ft_l:
                    method = getattr(fc, feature)
                    if feature == "first_peak":
                        bin_result.extend(method())
                    else:
                        bin_result.append(method())
                all_results.append(list(bin_result))
        return all_results

    def get_vector_by_streamer(self):
        pass

    def get_vector_feature(self, fc_l):
        df = self.pc.getSample()
        fc = FeaturesCalculation(df)
        results = []
        for feature in fc_l:
            method = getattr(fc, feature)
            results.append(method())
        return results

    def get_vector_feature_by_interval(self, interval, ft_l, is_skip, with_first_peak):
        ft = TopFeatures(self.pc.split(interval))
        ft.skip_first = is_skip
        results = []
        for feature in ft_l:
            method = getattr(ft, feature)
            if feature == "first_peak":
                if with_first_peak:
                    results.extend(method())
                else:
                    pass
            else:
                results.append(method())
        return results
