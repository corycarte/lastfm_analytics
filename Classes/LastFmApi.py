import yaml

class LastFmApi:

    _user = None
    _api_key = None

    def __init__(self, config_file: str):
        print("Loading configuration file {filename}".format(filename=config_file))
        

    def debug(self):
        print("Using LastFM to view\n\tuser: {user}\n\twith API Key: {key}".format(user=self._user, key=self._api_key))