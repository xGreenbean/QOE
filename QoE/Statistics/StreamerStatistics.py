""""""


class StreamerStatistics:
    def __init__(self):
        self.caught_in_time = []
        self.caught_in_server = []
        # list of tuples (captured, capturer)
        self.caught_in_threshold = []