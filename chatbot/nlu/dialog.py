from rasa_core.agent import Agent
from chatbot.config import Config
import logging

logger = logging.getLogger(__name__)


def load_agent(intent_classificator):
    conf = Config()
    logger.info('loading context model from: %s', conf.get_value('dialog-model-path'))
    return Agent.load(conf.get_value('dialog-model-path'), interpreter=intent_classificator)


def handle_message_input(context_agent, user_input):
    responses = context_agent.handle_message(user_input)

    # FIXME: We chose the first one, not the best heuristic.
    # FIXME: Harcoded fallback message.
    return responses[0] if responses else 'Sorry I cannot understand!'
