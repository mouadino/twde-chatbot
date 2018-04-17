#!/usr/bin/env python
import os

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy


def run():
    agent = Agent("resources/domain.yml",
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=RasaNLUInterpreter("resources/models/default/current"))

    agent.train_online("resources/data/stories.md",
                       input_channel=ConsoleInputChannel(),
                       max_history=2,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel=os.getenv('LOGLEVEL', 'ERROR'))
    run()
