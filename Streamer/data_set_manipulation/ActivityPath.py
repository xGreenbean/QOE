import os

class ActivityPath(object):
    def __init__(self, path):
        self.path = path

    def get_sessions_path(self):
        sessions_path = []
        for session_path in os.listdir(os.path.join(self.path, 'sessions')):
            sessions_path.append(os.path.join(self.path, 'sessions', session_path))
        return sessions_path

    def get_sni_csv_path(self):
        for fname in os.listdir(self.path):
            if fname.endswith('csv'):
                return os.path.join(self.path, fname)

    def get_pcap_path(self):
        for fname in os.listdir(self.path):
            if fname.endswith('pcap'):
                return os.path.join(self.path, fname)
