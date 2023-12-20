import requests
from bs4 import BeautifulSoup

# надо оформить в виде функции, которая на вход принимает url, 
# и максимальное кол-во желаемых страниц. 
# Возвращать должна iterable из html-страниц (str). 
# Тут кстати хорошо зайдёт генератор, 
# можно посмотреть мой пример с созвона.


def go_pages(url, count=100):
    title_begin = None
    title_str = None
    for page in range(1,count):
        try:
            title_begin = title_str
            response = requests.get(f'{url}{page}', timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            title_str = soup.find('titley').text
            if title_begin == title_str:
                break
        except(requests.RequestException, ValueError, AttributeError):
            return False
        yield soup




if __name__ in '__main__':
    url = 'https://www.olx.kz/zhivotnye/?page='
    go_pages(url)

# count = 1
# title_begin = None
# title_str = None

# while True:
#     title_begin = title_str
#     url = f'https://www.olx.kz/zhivotnye/?page={count}'
#     result = requests.get(url)
#     soup = BeautifulSoup(result.text, 'html.parser')
#     title_str = soup.find('title').text
#     if title_begin == title_str:
#         break
#     count +=1
#     print(title_str)

