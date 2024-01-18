from web_app.models import OlxSite
from web_app import db
from web_app.schema import Adv
from web_app.logger import logger


def insert_advertise(adv: Adv): 
    """ функция, которая сохраняет данные, полученные после парсинга, в бд"""
    
    if adv_exists(adv.url):
        logger.warning(f"adv already exists in DB, {adv.url}")
    adv_as_dict = adv.dict()
    parse_ad = OlxSite(**adv_as_dict)
    
    db.session.add(parse_ad)
    db.session.commit()


def extract_from_db():
    """функция, которая получает N <объектов> из бд"""
    ads_list = OlxSite.query.paginate(page=1, per_page=20)
    return ads_list


def adv_exists(url: str):
    """функция, которая проверяет есть ли объявление в базе"""
    count_results = OlxSite.query.filter(OlxSite.url == url).count()
    return bool(count_results)
  