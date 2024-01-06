from flask import Flask
from web_app.models import db
from flask import render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    return app
