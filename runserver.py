from web_app import db, create_app
from web_app.database_functions import parse_to_base








if __name__ == "__main__":
    app = create_app()
    app.app_context().push()
    db.create_all()
    parse_to_base()
            