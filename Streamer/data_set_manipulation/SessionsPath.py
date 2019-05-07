import os


class SessionsPath(object):
    def __init__(self, path):
        self.path = path

    def get_splits_path(self):
        sessions_path = []
        for session_path in sorted(os.listdir(os.path.join(self.path, 'splits'))):
            sessions_path.append(os.path.join(self.path, 'splits', session_path))
        return sessions_path

    def get_session_path(self):
        for fname in os.listdir(self.path):
            if fname.endswith('pcap'):
                return os.path.join(self.path, fname)
