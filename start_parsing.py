from parser.olx_parser import parser_category
from parser.database import Database
from web_app.app import create_app
from web_app.models import db, OlxSite
from web_app.user.views import blueprint as user_blueprint
from web_app.user.models import User
from flask_login import LoginManager


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()   
        app.register_blueprint(user_blueprint)
        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.login_view = 'user.login'

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(user_id)
        parser_db = Database(db, OlxSite)
        url = 'https://www.olx.kz/zhivotnye/?page='
        for adt_dataclass_instance in parser_category(url, parser_db):
            parser_db.insert_advertise(adt_dataclass_instance)

           
        