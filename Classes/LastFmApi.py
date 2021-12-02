import requests
import json

API_ROOT = "http://ws.audioscrobbler.com/2.0/"

class LastFmApi:

    _user = None
    _api_key = None

    def __init__(self, api_key: str):
        self._api_key = api_key

    def set_user(self, user: str):
        self._user = user

    def pull_last_days_songs(self, days: int) -> dict:
        if days < 1:
            return {}

        req_endpoint = API_ROOT + '?method=user.getrecenttracks&user={user_name}&api_key={key}&format=json'.format(user_name=self._user, key=self._api_key)
        response = requests.get(req_endpoint)

        if response.status_code == 200:
            res = json.loads(response.text)
            return res

        print("Error retrieving data: Status code {code}".format(code=response.status_code))
        return {}

    def debug(self):
        print("Using LastFM to view\n\tuser: {user}\n\twith API Key: {key}".format(user=self._user, key=self._api_key))