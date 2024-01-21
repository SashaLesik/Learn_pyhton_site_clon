from web_app.models import OlxSite
from web_app.models import db
from web_app.logger import logger
from sqlalchemy import desc




def extract_from_db():
    """функция, которая получает N <объектов> из бд"""
    ads_list = OlxSite.query.\
        order_by(desc(OlxSite.date_posted)).paginate(page=1, per_page=20)
    return ads_list


