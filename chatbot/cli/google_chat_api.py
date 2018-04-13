#!/usr/bin/env python3
import logging
import os

from flask import Flask, request, json

from .. import core


logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route('/', methods=['POST'])
def on_event():
    """Handles an event from Hangouts Chat."""
    event = request.get_json()
    logger.debug("received %s", event)
    if event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
        # TODO: Add a better welcoming message.
        response = 'Thanks for adding me to "%s"!' % event['space']['displayName']
    elif event['type'] == 'MESSAGE':
        response = core.handle_input(event['message']['text'])
    else:
        return
    logger.debug("sending %s", response)
    return json.jsonify({'text': response})


def run():
    port = os.environ.get('PORT', 8080)
    app.run(port=port, debug=True)


if __name__ == '__main__':
    run()
