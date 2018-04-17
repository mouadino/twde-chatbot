#!/usr/bin/env python3
import logging
import os

from flask import Flask, request, json, abort
from chatbot import config
from chatbot import core

logger = logging.getLogger(__name__)
app = Flask(__name__)
conf = config.Config()


def format_message(message):
    logger.debug("sending %s", message)
    return json.jsonify({'text': message})


def invalid_request(incoming_request):
    if not incoming_request.get_json():
        response = json.jsonify({'error': "Bad request"})
        response.status_code = 400
        return response

    event = incoming_request.get_json()
    logger.debug("received %s", event)
    logger.debug("token %s", conf.get_value("HANGOUTS_API_KEY"))

    if event.get('token') != conf.get_value("HANGOUTS_API_KEY"):
        response = json.jsonify({'error': "Wrong token"})
        response.status_code = 401
        return response
    if not event.get('type') or not event.get('message') or not event.get('space'):
        response = json.jsonify({'error': "Invalid request, type or message missing"})
        response.status_code = 400
        return response


@app.route("/" + conf.get_value("MESSENGER_ENDPOINT"), methods=['POST'])
def on_event():
    """Handles an event from Hangouts Chat."""
    invalid_request_response = invalid_request(request)
    if invalid_request_response:
        return invalid_request_response

    event = request.get_json()
    if event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
        return format_message('Thanks for adding me to "%s"!' % event['space']['displayName'])
    elif event['type'] == 'MESSAGE':
        return format_message(core.handle_input(event['message']['text']))
    else:
        abort(400)


def run():
    port = os.environ.get('PORT', 8080)
    app.run(port=port, debug=True)


if __name__ == '__main__':
    run()
