import requests
import time
from bs4 import BeautifulSoup
import csv
import base64
import re
import datetime
import sys
import time



from monitor_queue.parser import get_days, get_times
from monitor_queue.funcs import asleep, dt_now, aprint, aprint2, ainit,make_sckeernshot, h_now

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

DELAY_AFTER_ACTION=20
DELAY_ANALYSE=5
DELAY_WAIT=500 #1000
DELAY_BAD_CAPTCHA=120

WORK_START=0
WORK_END=25

FAST_START=2
FAST_END=18

VERYFAST0_HOUR=3
#VERYFAST0_MIN_START=50
#VERYFAST0_MIN_END=60

VERYFAST1_HOUR=4
#VERYFAST1_MIN_START=0
#VERYFAST1_MIN_END=0

VERYFAST2_HOUR=6
#VERYFAST2_MIN_START=0
#VERYFAST2_MIN_END=0

VERYFAST3_HOUR=7
#VERYFAST3_MIN_START=0
#VERYFAST3_MIN_END=0


DELAY_WAIT_VERYFAST=5
DELAY_WAIT_FAST=25
DELAY_WAIT_NORMAL=300 #Сессия заканчивается быстрее 1500сек(уточнить, поэтому ставить папарметр ниже)

BROWSER_LOAD_TIMEOUT = 30  # Adjust this value as needed

FORCE_RELOGIN=1800
login_timestamp = 1

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
text_wrong_number="введены не правильно"
text_waitlist="Вы записаны в список ожидания"
text_notime="Извините, но в настоящий момент на интересующее Вас консульское действие в системе предварительной записи нет свободного времени"
text_choose="Для записи на прием необходимо выбрать" # Внимание! Для записи на прием необходимо выбрать время приема и нажать кнопку "Записаться на прием"
text_wrong_something ="Something went wrong"
text_cant_be_reached = "site can't be reached"  



form1_captcha_answer_xpath="/HTML[1]/BODY[1]/DIV[1]/DIV[3]/FORM[1]/TABLE[1]/TBODY[1]/TR[1]/TD[2]/DIV[4]/INPUT[1]"
form1_captcha_solver_xpath="/html/body/div/div[3]/form/table/tbody/tr/td[2]/div[4]/div"
form1_submit_xpath="/html/body/div/div[3]/form/table/tbody/tr/td[2]/input"
form2_submit_xpath="/html/body/div/div[3]/form/table/tbody/tr/td[2]/input"

message_xpath="/html/body/div/div[3]/form/table/tbody/tr/td[2]/div[1]/span"

def do_postback(driver,num):
    js=f"javascript:__doPostBack('ctl00$MainContent$Calendar','{num}')"
    aprint(js)
    driver.execute_script(js)

def solver_get(driver):
    try:
        element = driver.find_element(By.XPATH, form1_captcha_solver_xpath)
        element_text = element.text
        return element_text
    except Exception as e:
        return "no solver"
    return "error get solver"

def solver_click(driver):
    try:
        element = driver.find_element(By.XPATH, form1_captcha_solver_xpath)
        driver.execute_script("arguments[0].click();", element)
        return "solver_clicked"
    except Exception as e:
        return f"solver_click- Произошла ошибка: {e}"
    return "error get solver"

def message_get(driver):
    try:
        element = driver.find_element(By.XPATH, message_xpath)
        element_text = element.text
        return element_text
    except Exception as e:
        return f"Произошла ошибка: {e}"
    return "error get text"

    
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
            aprint(capthca_answer_text)
            return capthca_answer_text
        aprint("captcha не введена")
        solver=solver_get(driver)
        aprint(solver)
        if "SLOT" in solver:
            solver_click(driver)
            asleep(2)
        asleep(1)

    aprint("captcha не введена в течение минуты")
    return ""

def open_browser(query,id):
    #query = f"about:blank"
    ainit(query,id)

    working_days=[]
    init=False

    while True:

        hnow=h_now()

        if((hnow<WORK_START) or (hnow>WORK_END)):
            asleep(321)
            continue
        aprint(dt_now())


        if ((hnow==VERYFAST0_HOUR) or (hnow==VERYFAST1_HOUR) or (hnow==VERYFAST2_HOUR) or (hnow==VERYFAST3_HOUR)):
            DELAY_WAIT=DELAY_WAIT_VERYFAST
        elif (hnow>=FAST_START) and (hnow<FAST_END):
            DELAY_WAIT=DELAY_WAIT_FAST
        else:
            DELAY_WAIT=DELAY_WAIT_NORMAL
    
        if(init==False):
            init=True
            aprint(query)
    
            print("Browser navigate", query, id)
            driver.get(query)  # Открытие страницы Google
            aprint("Мониторинг ситуации")

        try:
            element_present = WebDriverWait(driver, BROWSER_LOAD_TIMEOUT).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
        except TimeoutException:
            print("Timed out waiting for page to load")

        html_code=driver.page_source
        response_text=html_code
        soup = BeautifulSoup(html_code, 'html.parser')


        # aprint(response_text)
        current_url=driver.current_url


        if "blocked" in current_url:
            aprint("BLOCKED")
            #make_sckeernshot(driver)
            #driver.refresh()
            #aprint("refresh")
            sys.exit(1)
        if "/Visitor.aspx" in current_url:
            aprint("Session expired")
            aprint("reload")
            driver.get(query)
            asleep(DELAY_AFTER_ACTION)
            #make_sckeernshot(driver)
            #driver.refresh()
            #aprint("refresh")
        elif text_wrong_number in response_text:
            aprint("wrong number")
            aprint("reload")
            driver.get(query)
            asleep(DELAY_AFTER_ACTION)
        elif text_wrong_something in response_text:
            aprint("Something went wrong")
            make_sckeernshot(driver)
            #driver.refresh()
            #aprint("refresh")
            #asleep(DELAY_WAIT)
            aprint("reload")
            driver.get(query)
            #asleep(DELAY_AFTER_ACTION)
            aprint("nodelay, because probably update")

        #elif text_captcha in response_text:
        elif text_waitlist in response_text:
            aprint("Форма - вы в списке ожидания")
            message=message_get(driver)
            aprint(message)
            asleep(3)
            aprint("Нажимаем")
            do_send_form2(driver)
            #asleep(DELAY_AFTER_ACTION)

        elif text_fill in response_text:
            login_timestamp = int(time.time())
            aprint("Вводим капчу")
            
            captcha=wait_captcha(driver)
            if (re.match(r'^\d{6}$', captcha)):
                asleep(3)
                aprint("Нажимаем")
                do_send_form(driver)
                #asleep(DELAY_AFTER_ACTION)
            elif (captcha==""):
                aprint("no captcha result, wait and refresh")
                asleep(DELAY_BAD_CAPTCHA)
                driver.refresh()
                aprint("refresh")
                asleep(DELAY_AFTER_ACTION)
            else:
                aprint("wrong captcha, just refresh")
                driver.refresh()
                aprint("refresh")
                asleep(DELAY_AFTER_ACTION)                



        elif text_notime in response_text:
            aprint("Нет свободного времени => обновляем")
            #make_sckeernshot(driver)
            asleep(DELAY_WAIT)
            driver.refresh()
            aprint("refresh")
            asleep(DELAY_AFTER_ACTION)

        elif text_choose in response_text:
            aprint("choose_time -> action")
            #make_sckeernshot(driver)

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
        elif text_choose in text_cant_be_reached:
            aprint("something - text_cant_be_reached")
            make_sckeernshot(driver)
            asleep(DELAY_ANALYSE)
            aprint("refresh")
            driver.refresh()
            asleep(DELAY_ANALYSE)
        else:
            aprint("something else")
            make_sckeernshot(driver)
            #asleep(DELAY_WAIT)
            aprint("reload")
            driver.get(query)
            #asleep(DELAY_AFTER_ACTION)


        if (int(time.time())-login_timestamp>FORCE_RELOGIN):
            aprint("FORCE_RELOGIN")
            aprint("reload")
            driver.get(query)
            
        asleep(DELAY_ANALYSE)
'''
    except:
        aprint("except")
        asleep(60)
'''