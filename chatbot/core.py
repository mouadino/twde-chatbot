from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter


def get_agent():
    # FIXME: Hardcoded date of the model.
    interpreter = RasaNLUInterpreter("resources/models/default/current")
    return Agent.load("resources/models/dialogue", interpreter=interpreter)


def handle_input(user_input):
    agent = get_agent()
    responses = agent.handle_message(user_input)

    # FIXME: We chose the first one, not the best heuristic.
    # FIXME: Harcoded fallback message.
    return responses[0] if responses else 'Sorry I cannot understand!'
