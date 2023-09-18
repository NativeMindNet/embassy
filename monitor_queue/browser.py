import requests
import time
from bs4 import BeautifulSoup
import csv
import base64
import re
import datetime

from monitor_queue.parser import get_days, get_times
from monitor_queue.funcs import asleep, dt_now, aprint, aprint2, ainit,make_sckeernshot

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

DELAY_AFTER_ACTION=20
DELAY_ANALYSE=5
DELAY_WAIT=1000
DELAY_BAD_CAPTCHA=120

aprint("Init browser...")
#chrome_options = Options()
#chrome_options.add_argument("--headless")  # Запуск в фоновом режиме, без отображения окна браузера

# Настройка драйвера Chrome с указанием пути к расширению
chrome_options = webdriver.ChromeOptions()

extension_path = 'vendor/XEvilSolverPlugin.crx'
chrome_options.add_extension(extension_path)

#chrome_options.add_argument("--user-data-dir=../chrome")
#chrome_options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=chrome_options)

#text_captcha="Введите символы с картинки"
text_fill="Заполните поля информацией, полученной при оформлении записи"
text_waitlist="Вы записаны в список ожидания"
text_notime="Извините, но в настоящий момент на интересующее Вас консульское действие в системе предварительной записи нет свободного времени"
text_choose="Для записи на прием необходимо выбрать" # Внимание! Для записи на прием необходимо выбрать время приема и нажать кнопку "Записаться на прием"
text_wrong ="Something went wrong"

form1_captcha_answer_xpath="/HTML[1]/BODY[1]/DIV[1]/DIV[3]/FORM[1]/TABLE[1]/TBODY[1]/TR[1]/TD[2]/DIV[4]/INPUT[1]"
form1_submit_xpath="/html/body/div/div[3]/form/table/tbody/tr/td[2]/input"
form2_submit_xpath="/html/body/div/div[3]/form/table/tbody/tr/td[2]/input"

def do_postback(driver,num):
    js=f"javascript:__doPostBack('ctl00$MainContent$Calendar','{num}')"
    aprintjs)
    driver.execute_script(js)

def do_send_form(driver):
    #js='javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions("ctl00$MainContent$ButtonA", "", true, "", "", false, false))'
    #aprintjs)
    #driver.execute_script(js)
    #asleep(1)
    form1_submit_element = driver.find_element(By.XPATH, form1_submit_xpath)
    #form1_submit_element.submit()
    driver.execute_script("arguments[0].click();", form1_submit_element)
    asleep(1)

def do_send_form2(driver):
    form2_submit_element = driver.find_element(By.XPATH, form2_submit_xpath)
    driver.execute_script("arguments[0].click();", form2_submit_element)
    asleep(1)


def wait_captcha(driver):
    aprint("wait_captcha")

    for i in range(60):
        capthca_answer_element = driver.find_element(By.XPATH, form1_captcha_answer_xpath)
        capthca_answer_text = capthca_answer_element.get_attribute("value")
        if len(capthca_answer_text)>0:
            aprint("captcha введена")
            aprintcapthca_answer_text)
            return True
        aprint("captcha не введена")
        asleep(1)

    aprint("captcha не введена в течение минуты")
    return False

def open_browser(query,id):
    #query = f"about:blank"
    ainit(query,id)
    aprint(query)
    
    print("Browser navigate", query, id)
    driver.get(query)  # Открытие страницы Google
    aprint("Мониторинг ситуации")

    working_days=[]

    while True:
        aprint(dt_now())
        html_code=driver.page_source
        response_text=html_code
        soup = BeautifulSoup(html_code, 'html.parser')


        # aprint(response_text)


        if text_wrong in response_text:
            aprint("Something went wrong")
            make_sckeernshot(driver)
            #driver.refresh()
            #aprint("refresh")
            asleep(DELAY_WAIT)
            aprint("reload")
            driver.get(query)
            asleep(DELAY_AFTER_ACTION)

        #elif text_captcha in response_text:
        elif text_waitlist in response_text:
            aprint("Форма - вы в списке ожидания")
            asleep(3)
            aprint("Нажимаем")
            do_send_form2(driver)
            asleep(DELAY_AFTER_ACTION)

        elif text_fill in response_text:
            aprint("Вводим капчу")
            
            if wait_captcha(driver):
                asleep(3)
                aprint("Нажимаем")
                do_send_form(driver)
                asleep(DELAY_AFTER_ACTION)
            else:
                asleep(DELAY_BAD_CAPTCHA)
                driver.refresh()
                aprint("refresh")
                asleep(DELAY_AFTER_ACTION)




        elif text_notime in response_text:
            aprint("Нет свободного времени => обновляем")
            make_sckeernshot(driver)
            asleep(DELAY_WAIT)
            driver.refresh()
            aprint("refresh")
            asleep(DELAY_AFTER_ACTION)

        elif text_choose in response_text:
            aprint("choose_time -> action")
            make_sckeernshot(driver)

            working_days_before=working_days
            working_days=get_days(soup)

            aprint2("Working days:", working_days)

            times=get_times(soup)
            aprint(times)

            if(len(working_days_before)>0):
                if(working_days_before != working_days):
                    aprint2("Working days changed:", working_days)


            #asleep(500)
            #do_postback(driver,8656)
            #asleep(120)
            #do_postback(driver,8657)
            #asleep(120)
            #do_postback(driver,8658)
            #asleep(120)

            asleep(DELAY_WAIT)
            aprint("refresh")
            driver.refresh()
            asleep(DELAY_AFTER_ACTION)

        else:
            aprint("something else")
            make_sckeernshot(driver)
            asleep(DELAY_WAIT)
            aprint("reload")
            driver.get(query)
            asleep(DELAY_AFTER_ACTION)

        asleep(DELAY_ANALYSE)
'''
    except:
        aprint("except")
        asleep(60)
'''