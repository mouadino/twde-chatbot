import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.train import train_dialogue_model

from chatbot.config import CONF
from chatbot.nlu import intent_classificator


logger = logging.getLogger(__name__)
_AGENT = None


def get_agent():
    global _AGENT
    if not _AGENT:
        _AGENT = _load_agent(intent_classificator.load_classificator())
    return _AGENT


def _load_agent(intent_classificator):
    logger.info('loading context model from: %s', CONF.get_value('dialog-model-path'))
    return Agent.load(CONF.get_value('dialog-model-path'), interpreter=intent_classificator)


def handle_message_input(user_input):
    logger.debug('handling user input: %s', user_input)
    agent = get_agent()
    logger.debug('finished loading agent')
    responses = agent.handle_message(user_input)

    # FIXME: We chose the first one, not the best heuristic.
    # FIXME: Hardcoded fallback message.
    return responses[0] if responses else 'Sorry I cannot understand!'


def train_dialog():
    train_dialogue_model(CONF.get_value('domain-file'), CONF.get_value('stories-file'),
                         CONF.get_value('dialog-model-path'))


def train_dialog_online(intent_classificator, input_channel):
    agent = Agent(CONF.get_value('domain-file'), policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=intent_classificator)

    agent.train_online(CONF.get_value('stories-file'),
                       input_channel=input_channel,
                       max_history=CONF.get_value('dialog-model-max-history'),
                       batch_size=CONF.get_value('dialog-model-batch-size'),
                       epochs=CONF.get_value('dialog-model-epochs'),
                       max_training_samples=CONF.get_value('dialog-model-max-training-samples'))
    return agent
