#!/usr/bin/env python3
import os
from chatbot.messenger import google_chat_api

# Initialize the agent
google_chat_api.get_agent()
app = google_chat_api.app


def run():
    port = os.environ.get('PORT', 8080)
    app.run(port=port, debug=True)


if __name__ == '__main__':
    run()
