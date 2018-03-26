# Chatbot
This chatbot uses [Rasa](http://rasa.com/).

## Installation
Install rasa_core with `pip install rasa_core` <br/>

Install Spacy with medium sized modules:
```
pip install -U spacy
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```

Add the following to your shell config:
```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```
Install sklearn-crfsuite with `pip install -U sklearn_crfsuite` <br/>

## Train
Train the NLU model with `python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current` <br/>
Train the dialog model with `python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue` <br/>

## Run
Run server with `python -m rasa_core.server -d models/dialogue -u models/nlu/default/current` <br/>

## Play
Post request `curl -XPOST localhost:5005/conversations/default/parse -d '{"query":"greet"}'` <br/>

