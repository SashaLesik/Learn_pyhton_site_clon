import requests
from selenium_recaptcha_solver import RecaptchaSolver
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time



def get_product(url, count = 100):
    title_begin = None
    title_str = None
    count_contact = 1
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
                # response_product = requests.get('https://www.olx.kz' + card_url, timeout=5)
                # response_product.raise_for_status()                
                # soup_product = BeautifulSoup(response_product.text, 'lxml')
                ua = UserAgent().random
                options = Options()
                options.add_argument("--disable-blink-features=AutomationControlled")
                options.set_preference("dom.webdriver.enabled", False)
                options.set_preference("general.useragent.override", f"user-agent={ua}")

                driver = webdriver.Firefox(options=options)
                try:
                    driver.maximize_window()
                    driver.get(url='https://www.olx.kz' + card_url)
                    # time.sleep(8)
                    level = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/div/div')
                    driver.execute_script('arguments[0].scrollIntoView(true)', level)
                    time.sleep(8)
                    # <div class="recaptcha-checkbox-border" role="presentation"></div>
                    # button_captcha = driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()
                    button = driver.find_element(By.CLASS_NAME, 'css-1l3tcy7').click()
                    time.sleep(2)
            
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'lxml')

                    soup_product_number_phone = soup.find('a',class_='css-v1ndtc').text
                    # soup_product_number_phone = driver.find_element(By.CLASS_NAME, 'css-v1ndtc').text
                    # soup_product_number_phone = soup_product.find('a',class_='css-v1ndtc')
                    print(f'{soup_product_number_phone} контакт №{count_contact}')
                    count_contact += 1
                except(Exception) as ex:
                    print(ex)
                finally:
                    driver.close()
                    driver.quit()
        except(requests.RequestException, ValueError, AttributeError):
            print('error')
            continue
                #                     ua = UserAgent()
                # options = Options()
                # # options.add_argument("--headless")
                # # options.add_argument("--width=800")
                # # options.add_argument('--height=600')
                # options.set_preference("general.useragent.override", f"userAgent={ua}")
        


if __name__ in '__main__':
    url = 'https://www.olx.kz/zhivotnye/?page='
    get_product(url)
