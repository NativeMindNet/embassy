import re


def get_days(soup):
    date_links = soup.find_all('a', href=re.compile(r"javascript:__doPostBack\('.*','(\d+)'\)"))

    rabochie_dni = []
    nerabochie_dni = []

    for link in date_links:
        date = int(link.get_text())
        if link.find_parent('td', {'disabled': 'disabled'}):
            nerabochie_dni.append(date)
        else:
            rabochie_dni.append(date)

    #print("Рабочие дни:", rabochie_dni)
    #print("Нерабочие дни:", nerabochie_dni)
    return rabochie_dni

def get_times(soup):
    inputs = soup.find_all('input', {'name': 'ctl00$MainContent$RadioButtonList1'})
    result = [input['value'] for input in inputs]
    return result