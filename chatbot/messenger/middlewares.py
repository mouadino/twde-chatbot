import functools
import logging

from flask import request, json

from chatbot.config import CONF


logger = logging.getLogger(__name__)


def is_json(func):
    @functools.wraps(func)
    def inner(*args, **kw):
        if not request.get_json():
            response = json.jsonify({'error': "Bad request"})
            response.status_code = 400
            return response
        return func(*args, **kw)
    return inner


def authenticate(func):
    @functools.wraps(func)
    def inner(*args, **kw):
        event = request.get_json()
        logger.debug("received %s", event)
        logger.debug("token %s", CONF.get_value("hangouts-api-key"))

        if event.get('token') != CONF.get_value("hangouts-api-key"):
            response = json.jsonify({'error': "Wrong token"})
            response.status_code = 401
            return response
        return func(*args, **kw)
    return inner
