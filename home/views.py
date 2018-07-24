from os import path
from flask import Blueprint, send_from_directory, after_this_request
from common import SERVER_IP, SERVER_PORT


home_app = Blueprint('home_app', __name__)


@home_app.route('/favicon.ico')
def favicon():
    @after_this_request
    def add_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://{}:{}/demo/'.format(SERVER_IP, SERVER_PORT)
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return send_from_directory(path.join(home_app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@home_app.route('/DreamGame.js')
def dg_js():
    @after_this_request
    def add_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://{}:{}/demo/'.format(SERVER_IP, SERVER_PORT)
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return send_from_directory(path.join(home_app.root_path, 'static'), 'DreamGame.js')


@home_app.route('/DreamGame.pck')
def dg_pck():
    @after_this_request
    def add_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://{}:{}/demo/'.format(SERVER_IP, SERVER_PORT)
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return send_from_directory(path.join(home_app.root_path, 'static'), 'DreamGame.pck')


@home_app.route('/DreamGame.png')
def dg_png():
    @after_this_request
    def add_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://{}:{}/demo/'.format(SERVER_IP, SERVER_PORT)
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return send_from_directory(path.join(home_app.root_path, 'static'), 'demo.png')


@home_app.route('/DreamGame.wasm')
def dg_wasm():
    @after_this_request
    def add_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://{}:{}/demo/'.format(SERVER_IP, SERVER_PORT)
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return send_from_directory(path.join(home_app.root_path, 'static'), 'DreamGame.wasm')


@home_app.route('/')
def home():
    @after_this_request
    def add_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://{}:{}/demo/'.format(SERVER_IP, SERVER_PORT)
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return send_from_directory(path.join(home_app.root_path, 'static'), 'DreamGame.html')
