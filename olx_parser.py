from typing import TypedDict, NotRequired
import logging

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

month_mapping = {'январь': 'January',
                 'февраль': 'February',
                 'март': 'March',
                 'апрель': 'April',
                 'май': 'May',
                 'июнь': 'June',
                 'июль': 'July',
                 'август': 'August',
                 'сентябрь': 'September',
                 'октябрь': 'October',
                 'ноябрь': 'November',
                 'декабрь': 'December',
                 'января': 'January',
                 'февраля': 'February',
                 'марта': 'March',
                 'апреля': 'April',
                 'мая': 'May',
                 'июня': 'June',
                 'июля': 'July',
                 'августа': 'August',
                 'сентября': 'September',
                 'октября': 'October',
                 'ноября': 'November',
                 'декабря': 'December'}

class Adv(TypedDict):
    url: str
    id: str 
    ads_name: str
    ads_content: str
    phone_number: NotRequired[str]
    seller_name: str
    date_registered: datetime
    date_of_last_visit: datetime
    date_posted: datetime
    number_of_looks: NotRequired[int]
    location: NotRequired[str]
    picture: str

def translate_month_to_en(ru_month_name: str) -> str:
    # Функция перевода месяца с RU на EN
    return month_mapping[ru_month_name]


def parser_page(url):
    for page_num in range(1, 26):
        category_page_html = request_html(url=f'{url}{page_num}')
        adt_urls = extract_adt_urls(category_page_html)
        for adt_url in adt_urls:
            adv_html = request_html(adt_url)
            if adv_html is None:
                continue
            parser_adv = parser_adt(adv_html)
            if parser_adv is None:
                continue
            parser_adv['url'] = adt_url
            yield parser_adv


def request_html(url) -> str | None:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except(requests.RequestException, ValueError, AttributeError):
        print('error request_html')
        return None
    return response.text


def extract_adt_urls(category_page_html: str | None) -> list[str]:
    adt_urls = []
    if category_page_html is None:
        return adt_urls
    soup = BeautifulSoup(category_page_html, 'lxml')
    url_divs = soup.find_all('div', class_='css-1sw7q4x')
    for div in url_divs:
        try:
            card_url = div.find('a').get('href')
            if card_url:
                if 'https://' in card_url:
                    adt_urls.append(card_url)
                else:
                    adt_urls.append(f'https://www.olx.kz{card_url}')
        except Exception:
            print('error extract_adt_urls')
            continue
    print(adt_urls)
    return (adt_urls)


def parser_adt(adv_html: str) -> Adv | None:
    adv_html = BeautifulSoup(adv_html, 'lxml')
    try:
        soup_product_number_id = adv_html.find('span', class_='css-12hdxwj er34gjf0').text # ID объявления
        soup_product_name_salesman = adv_html.find('h4', class_='css-1lcz6o7 er34gjf0').text # Ник продавца
        soup_product_date_registered = adv_html.find('div', class_='css-16h6te1 er34gjf0').text 
        date_registered = parse_register_date(soup_product_date_registered) # Дата регистрации аккаунта
        soup_product_date_of_last_visit = adv_html.find('span', class_='css-1t0qnkx').text
        date_of_last_visit = parse_last_online_date(soup_product_date_of_last_visit) # Время последнего посещения сайта
        soup_product_date_posted = adv_html.find('span', class_='css-19yf5ek').text
        date_posted = parse_published_date(soup_product_date_posted) # Дата размещения объявления
        soup_product_jpg = adv_html.find('img').get('src') # Ссылка на фотографию объявления
        soup_product_title = adv_html.find('h4', class_='css-1juynto').text # Название объявления
        soup_product_text = adv_html.find('div', class_='css-1t507yq er34gjf0').text # Описание объявления   
    except(requests.RequestException, ValueError, AttributeError) as err:
        logging.error(f'{"_"*51}error adt{"_"*51}',  exc_info=err)
        return None
    adv = Adv(
            id=soup_product_number_id,
            ads_name=soup_product_title,
            ads_content=soup_product_text,
            seller_name=soup_product_name_salesman,
            date_registered=date_registered,
            date_of_last_visit=date_of_last_visit,
            date_posted=date_posted,
            picture=soup_product_jpg
        )
    return adv

def parse_register_date(date_time: str) -> datetime:
    #  Дата регистрации пользователя
    date_time = date_time.split(' ')
    result = f'{translate_month_to_en(date_time[2])}, {date_time[3]}'
    return datetime.strptime(result, '%B, %Y')


def parse_last_online_date(date_time: str) -> datetime:
    # Дата последнего посещения сайта пользователем
    date_time = date_time.split(' ')
    if len(date_time) > 4:
        day, month, year = date_time[1], translate_month_to_en(date_time[2]), date_time[3]
        date_of_last_visit = f'{day}, {month}, {year}'
        return datetime.strptime(date_of_last_visit, '%d, %B, %Y')
    elif len(date_time) == 3:
        day = str(datetime.now().day)
        month = str(datetime.now().month)
        year = str(datetime.now().year)
        time = date_time[2]
        date_of_last_visit = f'{day}, {month}, {year} {time}'
        return datetime.strptime(date_of_last_visit, '%d, %m, %Y %H:%M')
    elif len(date_time) == 4:
        day = str((datetime.now() - timedelta(days=1)).day)
        month = str(datetime.now().month)
        year = str(datetime.now().year)
        time = date_time[3]
        date_of_last_visit = f'{day}, {month}, {year} {time}'
        return datetime.strptime(date_of_last_visit, '%d, %m, %Y %H:%M')


def parse_published_date(date_time) -> datetime:
    # Дата публикации объявления
    date_time = date_time.split(' ')
    if date_time[0].isdigit():
        day = date_time[0]
        month = translate_month_to_en(date_time[1])
        year = date_time[2]
        published_date = f'{day} {month} {year}'
        return datetime.strptime(published_date, '%d %B %Y')
    elif date_time[0] == 'Сегодня':
        day = str(datetime.now().day)
        month = str(datetime.now().month)
        year = str(datetime.now().year)
        time = date_time[2]
        published_date = f'{day}, {month}, {year} {time}'
        return datetime.strptime(published_date, '%d, %m, %Y %H:%M')


if __name__ == '__main__':
    url = 'https://www.olx.kz/zhivotnye/?page='
    for adt_dict in parser_page(url):
        print(adt_dict)
        
