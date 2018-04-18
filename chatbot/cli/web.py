#!/usr/bin/env python3
import os

from werkzeug.contrib.profiler import ProfilerMiddleware

from chatbot.messenger import google_chat_api


app = google_chat_api.app
if os.getenv('FLASK_PROFILE'):
    app.config['PROFILE'] = True
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])


def run():
    port = os.getenv('PORT', 8080)
    app.run(port=port, debug=os.getenv('FLASK_DEBUG') == 'y')


if __name__ == '__main__':
    run()
