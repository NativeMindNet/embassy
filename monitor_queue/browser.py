import requests
import time
from bs4 import BeautifulSoup
import csv
import base64
import re
import datetime

import monitor_queue.parser
import monitor_queue.funcs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
#chrome_options.add_argument("--headless")  # Запуск в фоновом режиме, без отображения окна браузера
driver = webdriver.Chrome(options=chrome_options)


def asleep(sec):
    print("sleep ",sec)
    time.sleep(sec)

def dt_now():
    # Получаем текущую дату и время
    current_datetime = datetime.datetime.now()

    # Преобразуем объект datetime в строку для вывода
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime



def open_browser(query):
    #query = f"about:blank"
    print(query)
    
    driver.get(query)  # Открытие страницы Google
    print("Мониторинг ситуации")

    working_days=[]

    while True:
        print(dt_now())
        response_text=driver.page_source
        soup = BeautifulSoup(html_code, 'html.parser')


        # print(response_text)
        text_notime="Извините, но в настоящий момент на интересующее Вас консульское действие в системе предварительной записи нет свободного времени"
        text_choose="Для записи на прием необходимо выбрать" # Внимание! Для записи на прием необходимо выбрать время приема и нажать кнопку "Записаться на прием"

        
        if text_notime in response_text:
            print("Нет свободного времени => обновляем")
            driver.refresh()
            asleep(2*3600)

        if text_choose in response_text:
            print("choose_time -> action")

            working_days_before=working_days
            working_days=get_days(soup)

            print
            print("Working days:", working_days)

            if(len(working_days_before)>0):
                if(working_days_before != working_days):
                    print("Working days changed:", working_days)



            asleep(86400)
            #
            #driver.refresh()

        asleep(5)
'''
    except:
        print("except")
        asleep(60)
'''