from rasa_core.agent import Agent
from chatbot.config import Config
from rasa_core.train import train_dialogue_model
import logging

logger = logging.getLogger(__name__)


def load_agent(intent_classificator):
    conf = Config()
    logger.info('loading context model from: %s', conf.get_value('dialog-model-path'))
    return Agent.load(conf.get_value('dialog-model-path'), interpreter=intent_classificator)


def handle_message_input(context_agent, user_input):
    responses = context_agent.handle_message(user_input)

    # FIXME: We chose the first one, not the best heuristic.
    # FIXME: Hardcoded fallback message.
    return responses[0] if responses else 'Sorry I cannot understand!'


def train_dialog():
    conf = Config()
    train_dialogue_model(conf.get_value('domain-file'), conf.get_value('stories-file'),
                         conf.get_value('dialog-model-path'))
