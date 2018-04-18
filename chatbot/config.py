import json
import os


def uppercase(string):
    return string.upper().replace('-', '_')


def _load(config_file="/resources/default-config.json"):
    if os.getenv("CONFIG_FILE"):
        config_file = os.getenv("CONFIG_FILE")
    with open(os.getcwd() + config_file, 'r') as opened_file:
        return json.load(opened_file)


class _Config(object):
    def __init__(self):
        self._state = _load()

    def get_value(self, name):
        if os.getenv(uppercase(name)):
            return os.getenv(uppercase(name))
        else:
            return self._state[name]


CONF = _Config()
