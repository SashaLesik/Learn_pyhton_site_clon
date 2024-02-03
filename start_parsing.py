from parser.olx_parser import parser_category
from parser.database import Database
from web_app.app import create_app
from web_app.adverts.models import db, OlxSite


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        parser_db = Database(db, OlxSite)
        url = 'https://www.olx.kz/zhivotnye/?page='
        for adt_dataclass_instance in parser_category(url, parser_db):
            parser_db.insert_advertise(adt_dataclass_instance)
           
        