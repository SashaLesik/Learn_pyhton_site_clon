"""написать функцию на базе requests, 
которая заходит на сайт-жертву по ссылке, 
проверяет корректность ответа и возвращает HTML в виде строки"""

import requests


def get_olx(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    
if __name__ in '__main__':
    html = get_olx('https://www.olx.kz/')
    if html:
        with open('olx_clone.html', 'w', encoding='utf8') as f:
            f.write(html)