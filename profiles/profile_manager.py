import json
import os

class ProfileManager:
    def __init__(self, sessions_file='profiles/sessions.json'):
        self.sessions_file = sessions_file
        self.sessions = self._load_sessions()

    def _load_sessions(self):
        if os.path.exists(self.sessions_file):
            with open(self.sessions_file, 'r') as f:
                return json.load(f)
        return {}

    def save_session(self, name, session_data):
        self.sessions[name] = session_data
        with open(self.sessions_file, 'w') as f:
            json.dump(self.sessions, f, indent=4)

    def load_session(self, name):
        return self.sessions.get(name, None)

    def list_sessions(self):
        return list(self.sessions.keys())

    def delete_session(self, name):
        if name in self.sessions:
            del self.sessions[name]
            with open(self.sessions_file, 'w') as f:
                json.dump(self.sessions, f, indent=4)

