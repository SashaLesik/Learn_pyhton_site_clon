from parser.logger import logger
from parser.schema import Adv


class Database:

    def __init__(self, db, adv_table):
        self.db = db
        self.adv_table = adv_table

    def adv_exists(self, url: str):
        """функция, которая проверяет есть ли объявление в базе"""
        count_results = self.adv_table.query.\
            filter(self.adv_table.url == url).count()
        return bool(count_results)

    def insert_advertise(self, adv: Adv): 
        """ функция, которая сохраняет данные, полученные после парсинга, в бд"""

        if self.adv_exists(adv.url):
            logger.warning(f"adv already exists in DB, {adv.url}")
        adv_as_dict = adv.dict()
        parse_ad = self.adv_table(**adv_as_dict)

        self.db.session.add(parse_ad)
        self.db.session.commit()
