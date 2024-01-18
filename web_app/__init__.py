from flask import Flask
from web_app.models import db, OlxSite
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
        ads_list = extract_from_db() # order_by(OlxSite.date_posted.desc())
        return render_template('index.html', ads_list=ads_list)
    return app
      


    
            