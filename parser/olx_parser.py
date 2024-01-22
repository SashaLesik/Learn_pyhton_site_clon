
import requests
from bs4 import BeautifulSoup, Tag

from parser.detect_data import parse_register_date
from parser.detect_data import parse_last_online_date
from parser.detect_data import parse_published_date

from parser.database import Database
from parser.schema import Adv
from parser.logger import logger


def parser_category(url, parser_db: Database):
    for page_num in range(1, 26):
        category_page_html = request_html(url=f'{url}{page_num}')
        if category_page_html is None:
            logger.error(f'error on request category page {page_num}')
            continue
        adt_urls = extract_adt_urls(category_page_html)
        for adt_url in adt_urls:
            if parser_db.adv_exists(adt_url):
                continue
            adv_html = request_html(adt_url)
            if adv_html is None:
                continue
            parser_adv = parser_adt(adt_url, adv_html)
            if parser_adv is None:
                continue
            yield parser_adv


def request_html(url) -> str | None:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except(requests.RequestException, ValueError, AttributeError) as err:
        logger.error('error request_html', exc_info=err)
        return None
    return response.text


def extract_adt_urls(category_page_html: str | None) -> list[str]:
    adt_urls = []
    soup = BeautifulSoup(category_page_html, 'lxml')
    url_divs = soup.find_all(name='div', class_='css-1sw7q4x')
    print(url_divs)
    for div in url_divs:
        if not isinstance(div, Tag):
            continue
        try:
            card_url = div.find(name='a', class_='css-rc5s2u').get('href')
            print(card_url)
            if card_url:
                if 'https://' in card_url:
                    adt_urls.append(card_url)
                else:
                    adt_urls.append(f'https://www.olx.kz{card_url}')
        except Exception as err:
            logger.error('error extract_adt_urls', exc_info=err)
            continue
    print(adt_urls)
    return (adt_urls)


def parser_adt(url: str, adv_html: str) -> Adv | None:
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
        logger.error(f'{"_"*51}error adt{"_"*51}',  exc_info=err)
        return None
    adv = Adv(
            url=url,
            origin_id=soup_product_number_id,
            ads_name=soup_product_title,
            ads_content=soup_product_text,
            seller_name=soup_product_name_salesman,
            date_registered=date_registered,
            date_of_last_visit=date_of_last_visit,
            date_posted=date_posted,
            picture_url=soup_product_jpg
        )
    # print(adv)
    return adv

