#!/usr/bin/env python3
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_core.train import train_dialogue_model


def run():
    trainer = Trainer(RasaNLUConfig("resources/nlu_model_config.yaml"))
    training_data = load_data("resources/data/nlu.md")
    trainer.train(training_data)
    trainer.persist('resources/models/', fixed_model_name="current")
    train_dialogue_model("resources/domain.yml", "resources/data/stories.md", "resources/models/dialogue")


if __name__ == '__main__':
    run()
