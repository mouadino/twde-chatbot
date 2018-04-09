#!./venv/bin/python
# -*- coding: utf-8 -*-
import argparse
import logging

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_core.train import train_dialogue_model
from rasa_core.server import RasaCoreServer

parser = argparse.ArgumentParser(
    description='This is a chatbot for TWDE')
parser.add_argument('-p', '--port', nargs='?', default=5005,
                    help='Port: Specify port. Default is 8080')
parser.add_argument('-e', '--env', nargs='?', default="local",
                    help='Environment: Specify which config to load. Default is local.')
parser.add_argument('-w', '--workdir', nargs='?', default="./",
                    help='Workdir: Specify which working directory to use. Default is the local directory')
parser.add_argument('-v', '--verbose', nargs='?', const="DEBUG", default="WARN",
                    help='Lets you set the loglevel. Application default: WARN. Option default: DEBUG')  # without param->const. If no present->default
args = parser.parse_args()

log_level = logging.getLevelName(args.verbose)
logging.basicConfig(level=log_level,
                    datefmt='%d-%m %H:%M:%S',
                    format='%(asctime)s %(name)-s %(levelname)-s %(message)s')

print("\n\x1b[32mApplication staring...\x1b[0m")
print(" Port: " + str(args.port))
print(" Environment: " + str(args.env))
print(" Workdir: " + str(args.workdir))
print(" Logging: " + str(args.verbose))
print("\x1b[32m========================\x1b[0m")

trainer = Trainer(RasaNLUConfig("resources/nlu_model_config.json"))
training_data = load_data("resources/data/nlu.md")
trainer.train(training_data)
model_directory = trainer.persist('resources/models/')  # Returns the directory the model is stored in
train_dialogue_model("resources/domain.yml", "resources/data/stories.md", "resources/models/dialogue")

server = RasaCoreServer("resources/models/dialogue", model_directory)
logging.info("Starting server on port:%d",args.port)
server.app.run("0.0.0.0", args.port)

# app = create_app(port=args.port, environment=args.env, working_dir=args.workdir, greedy_mode=args.greedy)
# app.run(debug=True, use_reloader=False, port=args.port, host='0.0.0.0')
