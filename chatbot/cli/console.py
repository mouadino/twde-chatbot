#!/usr/bin/env python3
from rasa_core.channels.console import ConsoleInputChannel

from chatbot import core


def run():
    agent = core.get_agent()
    agent.handle_channel(ConsoleInputChannel())


if __name__ == '__main__':
    run()
