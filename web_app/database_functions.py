from web_app.models import OlxSite
from web_app import db
#from web_app import функция ктр напишет Kоля?


def parse_to_base(url, category, ads_name, ads_content, phone_number,
                  seller_name, date_registered,
                  date_of_last_visit, date_posted, number_of_looks, location, 
                  picture): 
    """ функция, которая сохраняет данные, полученные после парсинга, в бд"""
    ad_exists = OlxSite.query.filter(OlxSite.url == url).count()
    if not ad_exists:
        parse_ad = OlxSite(category=category, ads_name=ads_name,
                           ads_content=ads_content, phone_number=phone_number,
                           seller_name=seller_name,
                           date_registered=date_registered,
                           date_of_last_visit=date_of_last_visit,
                           date_posted=date_posted,
                           number_of_looks=number_of_looks, location=location,
                           picture=picture)
    # parse_ad = OlxSite(url = "example.com", category = "животные", ads_name = "продам корову",
    #                    ads_content =" 1234", phone_number ="9104398846", seller_name = "Vasio", date_registered = "11.12.2023", date_of_last_visit = "09.01.2024", 
    #                     date_posted = "08.01.2024", number_of_looks = 148, location = "Алматы",
    #                    picture = "href.example")
    
        db.session.add(parse_ad)
        db.session.commit()





def extract_from_db():
    """функция, которая получает N <объектов> из бд"""
    ads_list = OlxSite.query.all()
    return ads_list
    
    
  