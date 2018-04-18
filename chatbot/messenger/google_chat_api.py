import logging
import time

from flask import Flask, request, json, abort
import redis
from rq import Queue
from rq.job import Job

from chatbot.messenger import middlewares
from chatbot.nlu import dialog
from chatbot.config import CONF


app = Flask(__name__)
logger = logging.getLogger(__name__)
qconn = redis.from_url(CONF.get_value('redistogo-url'))
q = Queue('high', connection=qconn)


def format_message(message):
    logger.debug("sending %s", message)
    return json.jsonify({'text': message})


def _wait_for_response(job):
    # TODO: Can we do better then polling?
    while 1:
        logger.debug("poll worker for response with job_id=%s", job.get_id())
        job = Job.fetch(job.get_id(), connection=qconn)
        if job.is_finished:
            return str(job.result)
        if job.is_failed:
            raise Exception("job queue failed with id %s", job.get_id())
        time.sleep(0.5)


@app.route("/" + CONF.get_value("messenger-endpoint"), methods=['POST'])
@middlewares.authenticate
@middlewares.is_json
def on_event():
    """Handles an event from Hangouts Chat."""
    event = request.get_json()
    if event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
        return format_message('Thanks for adding me to "%s"!' % event['space']['displayName'])
    elif event['type'] == 'MESSAGE':
        job = q.enqueue(
            dialog.handle_message_input,
            event['message']['text']
        )
        reply = _wait_for_response(job)
        return format_message(reply)
    else:
        abort(400)
