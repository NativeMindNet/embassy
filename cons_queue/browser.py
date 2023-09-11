import requests
import time
from bs4 import BeautifulSoup
import csv
import base64


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
#chrome_options.add_argument("--headless")  # Запуск в фоновом режиме, без отображения окна браузера
driver = webdriver.Chrome(options=chrome_options)




def open_browser():
    query = f"about:blank"
    
    driver.get(query)  # Открытие страницы Google
    print("Ожидание отсутствия записи")

    while True:
        response_text=driver.page_source
        # print(response_text)
        text_notime="Извините, но в настоящий момент на интересующее Вас консульское действие в системе предварительной записи нет свободного времени"
        text_choose="Для записи на прием необходимо выбрать время приема и нажать кнопку" # Внимание! Для записи на прием необходимо выбрать время приема и нажать кнопку "Записаться на прием"

        
        if text_notime in response_text:
            print("Нет свободного времени => обновляем")
            driver.refresh()

        if text_choose in response_text:
            print("choose_time -> action")
            time.sleep(86400)
            #
            #driver.refresh()

        print("sleep")
        time.sleep(2*3600)
'''
    except:
        print("except, sleep 60")
        time.sleep(60)
'''