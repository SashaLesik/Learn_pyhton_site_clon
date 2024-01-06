from web_app import create_app
from web_app.models import db, OlxSite
#from web_app import  функция ктр напишет Kоля????


def parse_to_base(url, html): #добавить что именно импортиуертся вместо HTML
    """ функция, которая сохраняет данные, полученные после парсинга, в бд"""
    
    parse_ad = OlxSite(category = category, ads_name = ads_name,
                       ads_content = ads_content, phone_number = phone_number, raw_url_num_loc = raw_url_num_loc,
                       seller_name = seller_name, registration_date =registration_date,
                       number_of_looks = number_of_looks, location = location,
                       picture = picture)
    ad_exists = parse_ad.query.filter(parse_ad.url == url).count()
    if not ad_exists:
        db.session.add(parse_ad)
        db.session.commit()


def extract_from_db():
    """функция, которая получает N <объектов> из бд"""

    pass


if __name__ == "__main__":
    app = create_app()
    parse_to_base() #возможно надо добавить что-то еще
    app.run()