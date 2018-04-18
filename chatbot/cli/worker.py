#!/usr/bin/env python3
import redis
from rq import Worker, Queue, Connection

from chatbot.config import CONF


listen = ['low', 'medium', 'high']


def run():
    qconn = redis.from_url(CONF.get_value('redistogo-url'))
    with Connection(qconn):
        w = Worker(map(Queue, listen))
        w.work()


if __name__ == '__main__':
    run()