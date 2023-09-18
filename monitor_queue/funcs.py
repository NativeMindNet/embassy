import time
import datetime

query=""
id=""

def ainit(q,i):
    global query
    global id
    query=q
    id=i

def asleep(sec):
    aprint2("sleep ",sec)
    time.sleep(sec)

def dt_now():
    # Получаем текущую дату и время
    current_datetime = datetime.datetime.now()

    # Преобразуем объект datetime в строку для вывода
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

def aprint(text):
    global id
    global query
    print(dt_now(),text)

    with open(f"logs/{id}.txt", "a") as file:
        file.write(dt_now()+" "+str(text)+"\n")

def aprint2(text,text2):
    global id
    global query
    print(dt_now(),text,text2)

    with open(f"logs/{id}.txt", "a") as file:
        file.write(dt_now()+" "+str(text)+" "+str(text2)+"\n")

def make_sckeernshot(driver):
    global id
    global query
    dt=dt_now();
    filename=f"screenshots/{id}_{dt}.png"
    driver.save_screenshot(filename)