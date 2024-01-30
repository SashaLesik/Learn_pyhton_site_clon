from web_app.models import OlxSite
from sqlalchemy import desc




def extract_from_db():
    """функция, которая получает N <объектов> из бд"""
    ads_list = OlxSite.query.order_by(desc(OlxSite.date_posted))

    return ads_list


