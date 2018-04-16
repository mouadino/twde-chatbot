# Chatbot
This chatbot uses [Rasa](http://rasa.com/).

## Documentation
Right now the documentation only contains interesting links to get started with [docs](https://github.com/ThoughtWorksInc/twde-chatbot/tree/master/docs)

## Installation

### Prerequisite

Make sure that:

- You have python3.
- [pipenv](https://docs.pipenv.org/) is installed.
- Language setup correctly to english
```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Install

To install all dependencies execute:

```
pipenv install --dev
```

## Play

First you need to train the bot, to do that execute:

```
pipenv run chatbot/cli/train.py
```

Then to start the bot, there is multiple ways:

- In the console: ```pipenv run chatbot/cli/console.py```
- As a google chat api: ```pipenv run chatbot/cli/google_chat_api.py```
- As a google chat api using Heroku: ```pipenv run heroku local```


