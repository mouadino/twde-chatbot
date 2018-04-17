web: python -m spacy download en_core_web_md && pipenv run python -m spacy link --force en_core_web_md en  && ./chatbot/cli/train.py && gunicorn chatbot.messenger.google_chat_api:app
