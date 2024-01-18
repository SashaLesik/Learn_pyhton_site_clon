
from pydantic import BaseModel, Field
from datetime import datetime

class Adv(BaseModel):
    url: str = Field(description='url объявления')
    origin_id: str = Field(description='id объявления на сайте')
    ads_name: str = Field(description='Название объявления')
    ads_content: str = Field(description='Описание объявления')
    seller_name: str = Field(description='Ник продавца')
    date_registered: datetime = Field(description='Дата регистрации аккаунта')
    date_of_last_visit: datetime = Field(description='Время последнего посещения сайта')
    date_posted: datetime = Field(description='Дата размещения объявления')
    picture_url: str = Field(description='Ссылка на фотографию объявления')
    number_of_views: int = Field(description='Кол-во просмотров', default=0)
    location: str | None = Field(description='Местоположение объявления')
    phone_number: str | None = Field(description='Номер телефона')