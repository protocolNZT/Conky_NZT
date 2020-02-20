#!/usr/bin/python3

# € $

import requests
import re
import textwrap
from bs4 import BeautifulSoup as bs


headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/79.0.3945.130 Safari/537.36'}

base_url = 'https://www.cbr.ru/'


def finance_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        div = soup.find('div', id="widget_exchange").text
        title = str(textwrap.wrap(div))
        cource_txt = (title[3:14])
        date_daily = (title[20:30])
        date_now = (title[31:41])
        dollar_txt = (title[45:57])
        price_dollar_daily = (title[68:75])
        price_dollar_now = (title[86:94])
        euro_txt = (title[98:104])
        price_euro_daily = (title[115:122])
        price_euro_now = (title[133:141])

        file = open('/home/{user}/.config/conky/Conky_NZT/Conky_finance/usdeuro.txt', 'w')     # path to file
        file.write(cource_txt + ' на ' + date_now + '\n')
        file.write(dollar_txt + ' = ' + price_dollar_now + '.руб\n')
        file.write(euro_txt + ' = ' + price_euro_now + '.руб\n')

        file.write('\n' + cource_txt + ' на ' + date_daily + '\n')
        file.write(dollar_txt + ' = ' + price_dollar_daily + '.руб\n')
        file.write(euro_txt + ' = ' + price_euro_daily + '.руб\n')

        file.close()

    else:
        print('ERROR')


if __name__ == '__main__':
    finance_parse(base_url, headers)
