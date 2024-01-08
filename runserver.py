from web_app import db, create_app
from web_app.models import OlxSite
from sqlalchemy.orm import scoped_session, sessionmaker
#from web_app import функция ктр напишет Kоля?
from web_app import db, create_app

app = create_app()
app.app_context().push()
db.create_all()



def parse_to_base(): #добавить что именно импортиуертся 
    """ функция, которая сохраняет данные, полученные после парсинга, в бд"""
    
    # parse_ad = OlxSite(category = category, ads_name = ads_name,
    #                    ads_content = ads_content, phone_number = phone_number, raw_url_num_loc = raw_url_num_loc,
    #                    seller_name = seller_name, registration_date =registration_date,
    #                    number_of_looks = number_of_looks, location = location,
    #                    picture = picture)
    parse_ad = OlxSite(url = "example.com", category = "животные", ads_name = "продам корову",
                       ads_content =" 1234", phone_number ="9104398846", raw_url_num_loc = "example.com",
                       seller_name = "Vasio", registration_date = "11.12.2024",
                       number_of_looks = 148, location = "Алматы",
                       picture = "href.example")
    # ad_exists = parse_ad.query.filter(parse_ad.url == url).count()
    # if not ad_exists:
    db.session.add(parse_ad)
    db.session.commit()

parse_to_base()

def extract_from_db():
    """функция, которая получает N <объектов> из бд"""

    pass


# if __name__ == "__main__":
#     app = create_app()
#     app.app_context().push()
#     db.create_all()
#     parse_to_base() 
#     app.run()
            