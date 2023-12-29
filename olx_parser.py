import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


date = {'январь': 'January',
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


def get_product(url, count = 100):
    title_begin = None
    title_str = None
    for page in range(1,count):
        title_begin = title_str
        try:
            response = requests.get(f'{url}{page}', timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            title_str = soup.find('title').text
            if title_begin == title_str:
                break
            data = soup.find_all('div', class_='css-1sw7q4x')
            for link in data:
                card_url = link.find('a').get('href')
                response_product = requests.get('https://www.olx.kz' + card_url, timeout=5)
                response_product.raise_for_status()                
                soup_product = BeautifulSoup(response_product.text, 'lxml')
                soup_product_number_id = soup_product.find('span', class_='css-12hdxwj er34gjf0').text                 
                soup_product_name_salesman = soup_product.find('h4', class_='css-1lcz6o7 er34gjf0').text

                soup_product_date_registered = soup_product.find('div', class_='css-16h6te1 er34gjf0').text.split(' ')
                date_registered = format_date(soup_product_date_registered)
                

                soup_product_date_of_last_visit = soup_product.find('span', class_='css-1t0qnkx').text.split(' ')
                date_of_last_visit = format_date(soup_product_date_of_last_visit)
                
                soup_product_date_posted = soup_product.find('span', class_='css-19yf5ek').text.split(' ')
                date_posted = format_date(soup_product_date_posted)
                
                soup_product_jpg = soup_product.find('img').get('src')                  
                soup_product_title = soup_product.find('h4', class_='css-1juynto').text
                soup_product_text = soup_product.find('div', class_='css-1t507yq er34gjf0').text
        
        except(requests.RequestException, ValueError, AttributeError):
            print('error')
            continue



def format_date(date_time):
    '''['Member', 'Since', 'июнь', '2020', 'г.']'''
    day = None
    month = None
    year = None
    date_of_last_visit = None
    if date_time[0] == 'Member':
        result = f'{date[date_time[2]]}, {date_time[3]}'
        return datetime.strptime(result, '%B, %Y')

    elif date_time[0] == 'Онлайн':
        '''['Онлайн', '25', 'декабря', '2023', 'г.'] +
           ['Онлайн', 'в', '18:33'] +
           ['Онлайн', 'вчера', 'в', '07:04'] +
        '''
        if len(date_time) > 4:
            day, month, year = date_time[1], date[date_time[2]], date_time[3]
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

    elif date_time[0] == type(int):
        day = date_time[0]
        month = date[date_time[1]]
        year = date_time[2]
        date_of_last_visit = f'{day} {month} {year}'
        return datetime.strptime(date_of_last_visit, '%d %B %Y')
    elif date_time[0] == 'Сегодня':
        day = str(datetime.now().day)
        month = str(datetime.now().month)
        year = str(datetime.now().year)
        time = date_time[2]
        date_of_last_visit = f'{day}, {month}, {year} {time}'
        return datetime.strptime(date_of_last_visit, '%d, %m, %Y %H:%M')
    

if __name__ in '__main__':
    url = 'https://www.olx.kz/zhivotnye/?page='
    get_product(url)