from flask import Flask, request
from web_app.models import db
from flask import render_template
from flask_migrate import Migrate
from web_app.database_functions import extract_from_db
from web_app.user.views import blueprint as user_blueprint
from web_app.user.models import User
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
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
    def index():
        ads_list = extract_from_db()
        page = request.args.get('page', 1, type=int)
        pagination = ads_list.paginate(page=page, per_page=5)
        
        return render_template('index.html', pagination=pagination)
    return app


    
            