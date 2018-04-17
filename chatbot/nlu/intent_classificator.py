from rasa_core.interpreter import RasaNLUInterpreter
from chatbot.config import Config


def load_classificator():
    conf = Config()
    return RasaNLUInterpreter(conf.get_value('classification-model-path'))
