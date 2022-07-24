from flask import Flask 
import socket

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hello-app'

    @app.route('/')
    def home():
        stats = socket.gethostname()

        return f'Hello World!, from the {stats} container.'

    return app 

    