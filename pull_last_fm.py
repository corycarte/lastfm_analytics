import os



# Import local packages
from Classes.LastFmApi import LastFmApi as LastFm

if __name__ == '__main__':
    last_fm = LastFm("config.yaml")
    last_fm.debug()