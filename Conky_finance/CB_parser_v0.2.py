#!/usr/bin/python3
# € $
# import numpy as np
import sys
import time
import requests
import csv
from bs4 import BeautifulSoup

print(sys.version)
print(sys.executable)
print(time.strftime("%d-%m-%Y %H:%M"))

name_time_file = time.strftime("%d_%m_%Y")

base_url_eng = 'https://www.cbr.ru/eng/key-indicators/'  # English site locale
base_url_ru = 'https://www.cbr.ru/key-indicators/'  # Russian site locale

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (HTML, like Gecko) '
                         'Chrome/79.0.3945.130 Safari/537.36'
           }

files = 'usdeuro.txt'   # '/protocol/.config/conky/Conky_NZT/Conky_finance/usdeuro.txt'


def get_html(base_url, params=None):
    session = requests.Session()
    request = session.get(base_url, headers=headers, params=params)
    return request


def get_current_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    current_data = soup.find_all('tr')
    if len(current_data) >= 12:
        return len(current_data)
    else:
        return len(current_data)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='dropdown_content')
    global currency
    currency = []
    list_currency = []
    try:
        for item in items.find_all('div', class_='key-indicator_table_wrapper'):
            if item.get_text():
                list_currency.append((item.get_text().strip().split('\n', )))
            else:
                print(item.img.get('src'))
    except (RuntimeError, TypeError, NameError):
        print('Oops!  Something broke.  Try again...')

    currency.append(list_currency[0][0:1] + list_currency[0][2:3])
    currency.append(list_currency[0][7:8] + list_currency[0][12:13])
    currency.append(list_currency[0][17:18] + list_currency[0][22:23])

    currency.append(list_currency[0][0:1] + list_currency[0][1:2])
    currency.append(list_currency[0][7:8] + list_currency[0][11:12])
    currency.append(list_currency[0][17:18] + list_currency[0][21:22])

    currency.append(list_currency[1][0:2])
    currency.append(list_currency[1][6:8] + list_currency[1][10:11])
    currency.append(list_currency[1][15:17] + list_currency[1][19:20])
    currency.append(list_currency[1][24:26] + list_currency[1][28:29])
    currency.append(list_currency[1][33:35] + list_currency[1][37:38])

    return currency


def save_data(currency, files):
    with open(files, 'w') as txtfile:
        writer = csv.writer(txtfile)
        for line in currency:
            writer.writerow(line)


def parse_cbr():
    html = get_html(base_url_ru)
    if html.status_code == 200:
        current_data = get_current_data(html.text)
        if current_data >= 12:
            content_list = get_content(html.text)
            print(currency)
            print(f'List of: {int((len(content_list))) }', 'currencies')
            save_data(currency, files)
            print('Data saved to file:', files)
        else:
            print('Oops! The list is not valid.', f'Actual:{current_data}; Expected:{14};')
    else:
        print('Error status code site:', html.status_code)


parse_cbr()
