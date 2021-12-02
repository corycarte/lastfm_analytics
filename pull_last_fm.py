import os

import yaml

# Import local packages
from Classes.LastFmApi import LastFmApi as LastFm

def no_config_error():
    print("config.yaml doesn't exist")

if __name__ == '__main__':
    if not os.path.exists("config.yaml"):
        no_config_error()
        exit(1)

    user = api_key = time_range = None

    with open("config.yaml", "r") as stream:
        try:
            conf = yaml.safe_load(stream)
            print(conf)
            user = conf["user_name"]
            api_key = conf["api_key"]
            time_range = conf["default_time_range"]
        except yaml.YAMLError as exc:
            print(exc)

    last_fm = LastFm(api_key)
    last_fm.set_user(user)


    print(last_fm.pull_last_days_songs(0))
    print(last_fm.pull_last_days_songs(time_range))


    last_fm.debug()