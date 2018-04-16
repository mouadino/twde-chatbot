import json
import os


def _load(config_file="resources/default.json"):
    if os.getenv("CONFIG_FILE"):
        return json.load(os.getenv("CONFIG_FILE"))
    else:
        return json.load(config_file)


class Config(object):
    """
    Borg singleton config object
    """
    _state = _load()

    def __init__(self):
        self.__dict__ = self._state

    def get_value(self, name):
        if (os.getenv(name)):
            return os.getenv(name)
        else:
            return self._state[name]
