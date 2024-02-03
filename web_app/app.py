from flask import Flask
from web_app.adverts.models import db
from flask import render_template
from flask_migrate import Migrate

from web_app.adverts.views import blueprint as adverts_blueprint
from web_app.user.views import blueprint as user_blueprint
from web_app.user.models import User
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(adverts_blueprint)
    with app.app_context():
        db.create_all()
        app.register_blueprint(user_blueprint)
    migrate = Migrate(app, db, command='migrate')
        
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')

    def main():
        return render_template('main.html')


    return app
