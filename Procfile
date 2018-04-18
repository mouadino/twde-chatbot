worker: python -m spacy download en_core_web_md && pipenv run python -m spacy link --force en_core_web_md en  && ./chatbot/cli/train.py && ./chatbot/cli/worker.py
web: gunicorn --timeout=190 chatbot.cli.web:app
