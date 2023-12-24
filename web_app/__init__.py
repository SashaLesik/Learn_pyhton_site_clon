from flask import Flask
from sqlalchemy import create_engine
from web_app.config import DB_USER, DB_PASSWORD
from flask_sqlalchemy import SQLAlchemy
from web_app.models import db


DATABASE = 'postgres'
HOST = 'localhost'
PORT = '5433'

connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DATABASE}'

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    engine = create_engine(connection_string)
    db.init_app(app)
    @app.route('/')
    def index():
        return 'hello, word'
    return app



    
    
