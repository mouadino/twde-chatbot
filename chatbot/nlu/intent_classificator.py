from rasa_core.interpreter import RasaNLUInterpreter
from chatbot.config import Config
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer


def load_classificator():
    conf = Config()
    return RasaNLUInterpreter(conf.get_value('classification-model-path'))


def train_classificator():
    conf = Config()
    trainer = Trainer(RasaNLUConfig(conf.get_value('nlu-config-file-path')))
    training_data = load_data(conf.get_value('nlu-training-data-path'))
    trainer.train(training_data)
    trainer.persist(conf.get_value('models-directory'), fixed_model_name=conf.get_value('classification-model-name'))
