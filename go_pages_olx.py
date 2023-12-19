import requests
from bs4 import BeautifulSoup


count = 1
title_begin = None
title_str = None

while True:
    title_begin = title_str
    url = f'https://www.olx.kz/stroitelstvo-remont/otoplenie/?page={count}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    title_str = soup.find('title').text
    if title_begin == title_str:
        break
    count +=1
    print(title_str)

