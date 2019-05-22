
    def getSample(self):
        return self.sess_break()

    def split(self, intervals):
        request_response = self.sess_break()
        counter = 0
        frames = []
        request_response_list = []
        for sample in request_response:
            counter += 1
            frames.append(sample)
            if counter%intervals == 0:
                result = pd.concat(frames)
                request_response_list.append(result)
        return request_response_list
