import configparser
def read(config_file):
    config=configparser.ConfigParser()
    config.read(config_file)
    return config
