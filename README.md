# Chatbot
This chatbot uses [Rasa](http://rasa.com/).

## Documentation
Right now the documentation only contains interesting links to get started with [docs](https://github.com/ThoughtWorksInc/twde-chatbot/tree/master/docs)

## Installation
Run the setup script:
```bash
./setup.sh
```

Additionally you might want to set your locales (in most cases not needed):
```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

## Run
Switch to the previously installed virtual environment:
```bash
source venv/bin/activate
```

Then just run the run.py in your virtual environment:  
```bash
python run.py
```

This will expose the server on port _5005_

## Play
Post request `curl -XPOST localhost:5005/conversations/default/parse -d '{"query":"greet"}'` <br/>

## Tests
Tests can be executed with:
```bash
./run-tests.sh
```
