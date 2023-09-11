import time
import datetime


def asleep(sec):
    print("sleep ",sec)
    time.sleep(sec)

def dt_now():
    # Получаем текущую дату и время
    current_datetime = datetime.datetime.now()

    # Преобразуем объект datetime в строку для вывода
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime
