# Chatbot
This chatbot uses [Rasa](http://rasa.com/).

## Documentation
Right now the documentation only contains interesting links to get started with [docs](https://github.com/ThoughtWorksInc/twde-chatbot/tree/master/docs)

## Installation

### Prerequisite

Make sure that:

- You have python3.
- [pipenv](https://docs.pipenv.org/) is installed, if not run `pip install pyenv`.
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

First you need to train the bot, to do start by downloading language dependencies (this only need to be done once):

```
pipenv run python -m spacy download en_core_web_md
pipenv run python -m spacy link en_core_web_md en
```

Then run training using:

```
pipenv run chatbot/cli/train.py
```

*Note*: Currently training fails the first time it's run, so please run the command above a second time.

Then to start the bot, there is multiple ways:

- In the console: ```pipenv run chatbot/cli/console.py```
- As a google chat api: ```pipenv run chatbot/cli/google_chat_api.py```
- As a google chat api using Heroku: ```pipenv run heroku local```

To reduce logging verbosity set the environment variable LOGLEVEL to error, for example:

```
LOGLEVEL=ERROR pipenv run chatbot/cli/console.py
```

## Test

To run tests use:

```bash
pipenv run pytest
```

