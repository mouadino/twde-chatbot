from rasa_core.agent import Agent
from chatbot.config import Config


def load_agent(intent_classificator):
    conf = Config()
    return Agent.load(conf.get_value('dialog-model-path'), interpreter=intent_classificator)


def handle_message_input(context_agent, user_input):
    responses = context_agent.handle_message(user_input)

    # FIXME: We chose the first one, not the best heuristic.
    # FIXME: Harcoded fallback message.
    return responses[0] if responses else 'Sorry I cannot understand!'
