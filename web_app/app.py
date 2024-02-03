from flask import Flask
from web_app.adverts.models import db
from flask import render_template
from flask_migrate import Migrate

from web_app.adverts.views import blueprint as adverts_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(adverts_blueprint)
    with app.app_context():
        db.create_all()
    migrate = Migrate(app, db, command='migrate')

    @app.route('/')
    def main():
        return render_template('main.html')

    return app
