from flask import Flask, request
from web_app.models import db
from flask import render_template
from flask_migrate import Migrate
from web_app.database_functions import extract_from_db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    migrate = Migrate(app, db, command='migrate')

    @app.route('/')
    def index():
        ads_list = extract_from_db()
        page = request.args.get('page', 1, type=int)
        pagination = ads_list.paginate(page=page, per_page=5)
        
        return render_template('index.html', pagination=pagination)
    return app
      


    
            