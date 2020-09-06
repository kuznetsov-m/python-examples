import os

from config import Config

config_file = 'config.json'
credentials_file = 'credentials.json'

config = Config()
print(config.cloud_dir)
config.replace_from_file(config_file)
print(config.cloud_dir)
config.replace_from_file(credentials_file)