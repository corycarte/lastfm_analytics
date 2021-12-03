import os
import datetime as DT

import yaml

# Import local packages
from Classes.LastFmApi import LastFmApi as LastFm
import save_data as save

def no_config_error():
    print("config.yaml doesn't exist")

if __name__ == '__main__':
    if not os.path.exists("config.yaml"):
        no_config_error()
        exit(1)

    user = api_key = time_range = None
    today = DT.datetime.now()

    with open("config.yaml", "r") as stream:
        try:
            conf = yaml.safe_load(stream)
            user = conf["user_name"]
            api_key = conf["api_key"]
            time_range = conf["default_time_range"]
            output_dir = conf["output_dir"]
            last_pull_date = conf["last_pull_date"]
        except yaml.YAMLError as exc:
            print(f'Configuration Load Error: {exc}')
            exit(1)

    try:
        last_fm = LastFm(api_key)
        last_fm.set_user(user)

        tracklist = last_fm.pull_since(last_pull_date)
    except Exception as ex:
        print(f'LastFMApi Error: {ex}')

    outfile = os.path.join(output_dir, f'{today.strftime("%Y%m%d-%H%M")}_last_fm_data_pull.csv')
    save.setup_out_dir(output_dir)
    save.save_csv(tracklist, outfile)

    with open("config.yaml", "w") as update_config:
        conf["last_pull_date"] = today
        yaml.dump(conf, update_config, default_flow_style=False)