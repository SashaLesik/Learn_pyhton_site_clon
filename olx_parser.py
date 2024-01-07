import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


month_mapping  = {'январь': 'January',
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

def translate_month_to_en(ru_month_name: str) -> str:
    # Функция перевода месяца с RU на EN
    return month_mapping[ru_month_name]


def parser_page(url):
    for page_num in range(1,26): 
        category_page_html = request_html(url=f'{url}{page_num}') 
        adt_urls = extract_adt_urls(category_page_html) 
        for adt_url in adt_urls: 
            yield parser_adt(adt_url)


def request_html(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='css-1sw7q4x')
        return data
    except(requests.RequestException, ValueError, AttributeError):
        print('error request_html')


def extract_adt_urls(category_page_html):
    adt_urls = []
    for link in category_page_html:
        try:
            card_url = link.find('a').get('href')
            response_product = requests.get('https://www.olx.kz' + card_url, timeout=5)
            response_product.raise_for_status()
            soup_product = BeautifulSoup(response_product.text, 'lxml')
            adt_urls.append(soup_product)
        except(requests.RequestException, ValueError, AttributeError):
            print('error extract_adt_urls')
            continue
    print(adt_urls)

def parser_adt(adt_url):
    try:
        soup_product_number_id = adt_url.find('span', class_='css-12hdxwj er34gjf0').text                 
        soup_product_name_salesman = adt_url.find('h4', class_='css-1lcz6o7 er34gjf0').text
        soup_product_date_registered = adt_url.find('div', class_='css-16h6te1 er34gjf0').text
        date_registered = parse_register_date(soup_product_date_registered)                
        soup_product_date_of_last_visit = adt_url.find('span', class_='css-1t0qnkx').text
        date_of_last_visit = parse_last_online_date(soup_product_date_of_last_visit)                
        soup_product_date_posted = adt_url.find('span', class_='css-19yf5ek').text
        print(f'Проверка времени размещения: {soup_product_date_posted}')
        date_posted = parse_published_date(soup_product_date_posted)                
        soup_product_jpg = adt_url.find('img').get('src')                  
        soup_product_title = adt_url.find('h4', class_='css-1juynto').text
        soup_product_text = adt_url.find('div', class_='css-1t507yq er34gjf0').text
        print(f'!!!!!!!!!!!!!!!!Объявление!!!!!!!!!!!!!!!!')
        print(f'ID объявления: {soup_product_number_id}')
        print(f'Ник продавца: {soup_product_name_salesman}')
        print(f'Дата регистрации аккаунта: {date_registered}')
        print(f'Время последнего посещения сайта: {date_of_last_visit}')
        print(f'Дата размещения объявления: {date_posted}')
        print(f'Ссылка на фотографию объявления: {soup_product_jpg}')
        print(f'Название объявления: {soup_product_title}')
        print(f'Описание объявления: {soup_product_text}')  
        print('-----------------------')
  
    except(requests.RequestException, ValueError, AttributeError):
        print(f'___________________________________________________error adt___________________________________________________')
        
        
        



def parse_register_date(date_time: str) -> datetime:
    #  Дата регистрации пользователя
    date_time = date_time.split(' ')
    result = f'{translate_month_to_en(date_time[2])}, {date_time[3]}'
    return datetime.strptime(result, '%B, %Y')
    
def parse_last_online_date(date_time: str) -> datetime:
    # Дата последнего посещения сайта пользователем
    date_time = date_time.split(' ')
    day = None
    month = None
    year = None
    date_of_last_visit = None
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
    day = None
    month = None
    year = None
    published_date = None
    if int(date_time[0]):
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
    

if __name__ in '__main__':
    url = 'https://www.olx.kz/zhivotnye/?page=' 
    parser_page(url)