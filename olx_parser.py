import requests
from bs4 import BeautifulSoup

# '''написать функцию, которая с помощью requests 
# переходит по ссылке на товар и возвращает 
# HTML проверяя корректность ответа

# + название объявления - varchar/str - soup_product_title
# + описание объявления - varchar/str - soup_product_text
# - номер телефона в объявлении 
# + номер id объявления - varchar/str - soup_product_number_id
# + информация о продавце (имя - varchar/str - soup_product_name_salesman, 
#  с какого времени зарегистрирован на сайте - varchar/str - soup_product_date_registered, 
#  когда последний раз был в сети - varchar/str - soup_product_date_of_last_visit) 
# - количество просмотров объявления!!!
# - место объявления - varchar/str!!!
# + дата объявления - timestamp / datetime - soup_product_date_posted
# + И что-то, куда будет относиться картинка объявления - через 
# ссылку, как понимаю, то есть тоже varchar/str - soup_product_jpg
# '''



def get_product(url, count = 100):
    title_begin = None
    title_str = None
    for page in range(1,count):
        title_begin = title_str
        try:
            response = requests.get(f'{url}{page}', timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            title_str = soup.find('title').text
            if title_begin == title_str:
                break
            data = soup.find_all('div', class_='css-1sw7q4x')
            for link in data:
                card_url = link.find('a').get('href')
                response_product = requests.get('https://www.olx.kz' + card_url, timeout=5)
                response_product.raise_for_status()                
                soup_product = BeautifulSoup(response_product.text, 'html.parser')
                soup_product_number_id = soup_product.find('span', class_='css-12hdxwj er34gjf0').text    
                soup_product_name_salesman = soup_product.find('h4', class_='css-1lcz6o7 er34gjf0').text
                soup_product_date_registered = soup_product.find('div', class_='css-16h6te1 er34gjf0').text
                soup_product_date_of_last_visit = soup_product.find('span', class_='css-1t0qnkx').text

                soup_product_number_of_views = soup_product.findAllNext('div', class_='css-ayk4fp') # Вот эти данные не получается достать
                soup_product_location = soup_product.find('p', class_='css-1cju8pu er34gjf0').text # Вот эти данные не получается достать

                soup_product_date_posted = soup_product.find('span', class_='css-19yf5ek').text                
                soup_product_jpg = soup_product.find('img').get('src')                  
                soup_product_title = soup_product.find('h4', class_='css-1juynto').text
                soup_product_text = soup_product.find('div', class_='css-1t507yq er34gjf0').text
                    
                
        except(requests.RequestException, ValueError, AttributeError):
            continue
        
        
if __name__ in '__main__':
    url = 'https://www.olx.kz/zhivotnye/?page='
    print(get_product(url))