import os
import random
import logging
from bottle import Bottle
from bottle import HTTPError
from bottle import request
#from bottle import route
#from bottle import run
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(dsn=os.environ.get('SENTRY_DSN'), integrations=[BottleIntegration()])

app = Bottle()

beginnings = [
    "В то же время,",
    "Вместе с тем,",
    "Коллеги,",
    "Однако,",
    "С другой стороны,",
    "Следовательно,",
    "Соответственно,",
    "Тем не менее,",
]

subjects = [
    "диджитализация бизнес-процессов",
    "контекст цифровой трансформации",
    "парадигма цифровой экономики",
    "прагматичный подход к цифровым платформам",
    "программа прорывных исследований",
    "совокупность сквозных технологий",
    "ускорение блокчейн-транзакций",
    "экспоненциальный рост Big Data",
]

verbs = [
    "выдвигает новые требования",
    "заставляет искать варианты",
    "не оставляет шанса для",
    "несет в себе риски",
    "обостряет проблему",
    "открывает новые возможности для",
    "повышает вероятность",
    "расширяет горизонты",
]

actions = [
    "бюджетного финансирования",
    "дальнейшего углубления",
    "компрометации конфиденциальных",
    "несанкционированной кастомизации",
    "нормативного регулирования",
    "практического применения",
    "синергетического эффекта",
    "универсальной коммодизации",
]

ends = [
    "внезапных открытий.",
    "волатильных активов.",
    "государственно-частных партнёрств.",
    "знаний и компетенций.",
    "нежелательных последствий.",
    "непроверенных гипотез.",
    "опасных экспериментов.",
    "цифровых следов граждан.",
]

def generate_speech():
    speech = ' '.join([
        random.choice(beginnings),
        random.choice(subjects),
        random.choice(verbs),
        random.choice(actions),
        random.choice(ends)
        ])
    return speech

@app.route('/')
def server_root():
    with open('index.html', 'r', encoding='UTF-8') as INDEX_FILE:
        R_OUTPUT = INDEX_FILE.read()
    return R_OUTPUT

@app.route('/voting/vote')
def vote_for():
    with open('./vote.html', 'r', encoding='UTF-8') as VOTE_FILE:
        V_OUTPUT = VOTE_FILE.read()
    return V_OUTPUT

@app.route('/voting/result')
def vote_res():
    with open('./result.html', 'r', encoding='UTF-8') as VRES_FILE:
        W_OUTPUT = VRES_FILE.read()
    return W_OUTPUT

@app.route('/success')
def success_dir():
    with open('success.html', 'r', encoding='UTF-8') as SUCCESS_FILE:
        S_OUTPUT = SUCCESS_FILE.read()
    return S_OUTPUT

@app.route('/fail')
def fail_dir():
    raise RuntimeError('There is an error of /fail and Heroku')

@app.route('/crash')
def crash_dir():
    C_OUTPUT = HTTPError(500, 'Internal Server Error')
    return C_OUTPUT

@app.route('/api/generate/')
def gen_one():
    _OUTPUT_ONE = {}
    _OUTPUT_ONE['message'] = generate_speech()
    return _OUTPUT_ONE

@app.route('/api/generate/<number:int>')
def gen_few(number):
    _OUTPUT_FEW = {}
    _OUTPUT_FEW['messages'] = [ generate_speech() for _X in range(number) ]
    return _OUTPUT_FEW

if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), server='gunicorn', workers=2)
    else:
        app.run(host='localhost', port=8080, debug=True)
