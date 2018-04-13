#!/usr/bin/env python3
import os
import logging

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_core.train import train_dialogue_model

from spacy.cli.download import download
from spacy.cli.link import link


logger = logging.getLogger(__name__)


def _download_spacy_data():
    download('en_core_web_md')
    # FIXME: Sometimes this fail!
    link('en_core_web_md', 'en', force=True)


def _train():
    trainer = Trainer(RasaNLUConfig("resources/nlu_model_config.json"))
    training_data = load_data("resources/data/nlu.md")
    trainer.train(training_data)
    trainer.persist('resources/models/', fixed_model_name="current")
    train_dialogue_model("resources/domain.yml", "resources/data/stories.md", "resources/models/dialogue")


def run():
    if os.environ.get('DOWNLOAD_SPACY_DATA') != 'n':
        logger.info('Downloading spacy data ...')
        _download_spacy_data()

    logger.info('Training model ...')
    _train()


if __name__ == '__main__':
    run()
