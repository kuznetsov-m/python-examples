import os
import json

class BaseConfig():
    def __init__(self):
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        for member in members:
            if member in os.environ:
                setattr(self, member, os.environ[member])

    def replace_from_file(self, path: str):
        f = open(path, 'r')
        config = json.load(f)
        f.close()
        
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

        for key in config.keys():
            if key in members:
                setattr(self, key, config[key])