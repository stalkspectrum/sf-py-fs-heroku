import os
import random
from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

@route('/')
def server_root():
    with open('index.html', 'r', encoding='UTF-8') as INDEX_FILE:
        OUTPUT_ = INDEX_FILE.read()
    return OUTPUT_


if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), server=gunicorn, workers=2)
    else:
        run(host='localhost', port=8080, debug=True)
