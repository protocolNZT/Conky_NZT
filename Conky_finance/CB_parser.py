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
        line_date = soup.find('div', id="widget_exchange").text

        re_tex = re.findall(r'\w+', line_date)
        course = re_tex[0]
        currencies = re_tex[1]
        dollar_text = re_tex[8]
        dollar_usa = re_tex[9]
        rub = re_tex[10]
        euro_text = re_tex[16]

        re_tex_date = re.findall(r'\d+', line_date)
        day_daily = re_tex_date[0]
        mount_daily = re_tex_date[1]
        yuer_daily = re_tex_date[2]

        day_now = re_tex_date[3]
        mount_now = re_tex_date[4]
        yuer_now = re_tex_date[5]

        dollar_daily = re_tex_date[6]
        dollar_daily_ = re_tex_date[7]
        dollar_now = re_tex_date[8]
        dollar_now_ = re_tex_date[9]

        euro_daily = re_tex_date[10]
        euro_daily_ = re_tex_date[11]
        euro_now = re_tex_date[12]
        euro_now_ = re_tex_date[13]

        file = open('/YOU PATH/.config/conky/Conky_NZT/Conky_finance/usdeuro.txt', 'w')     # path to file
        file.write(course + ' ' + currencies + ' на ' + day_now + '.' + mount_now + '.' + yuer_now + '\n')

        doll_now = dollar_now + dollar_now_
        doll_daily = dollar_daily + dollar_daily_

        dollar_how_up = int(doll_now) - int(doll_daily)

        if doll_now > doll_daily:
            dollar_now_up = '➚'
            dollar_how_up = int(doll_now) - int(doll_daily)
            doll_how_up_fl = (str(0) + '.' + str(dollar_how_up))
            file.write('$ ' + dollar_text + ' ' + dollar_usa + ' = ' + dollar_now + '.' + dollar_now_ + rub +
                       ' ' + dollar_now_up  + ' +' + doll_how_up_fl + '\n')

        elif doll_now < doll_daily:
            dollar_now_down = '➘'
            dollar_how_down = int(doll_now) - int(doll_daily)
            dollar_absolut_func = (abs(dollar_how_down))
            doll_how_down_fl = (str(0) + '.' + str(dollar_absolut_func))
            file.write('$ ' + dollar_text + ' ' + dollar_usa + ' = ' + dollar_now + '.' + dollar_now_ + rub +
                       ' ' + dollar_now_down + ' -' + doll_how_down_fl + '\n')

        elif doll_now == doll_daily:
            dollar_now_balans = '☯'
            dollar_how_balans= int(doll_now) - int(doll_daily)
            doll_how_balans_fl = (str(0) + '.' + str(dollar_how_balans))
            file.write('$ ' + dollar_text + ' ' + dollar_usa + ' = ' + dollar_now + '.' + dollar_now_ + rub +
                       ' ' + dollar_now_balans  + ' ==' + doll_how_balans_fl + '\n')

        eur_now = euro_now + euro_now_
        eur_deily = euro_daily + euro_daily_

        if eur_now > eur_deily:
            eur_now_up = '➚'
            euro_how_up = int(eur_now) - int(eur_deily)
            euro_how_up_fl = (str(0) + '.' + str(euro_how_up))
            file.write('€ ' + euro_text + ' = ' + euro_now + '.' + euro_now_ + rub + ' ' + eur_now_up +
                       ' +' + euro_how_up_fl + '\n')

        elif eur_now < eur_deily:
            eur_now_down = '➘'
            euro_how_down = int(eur_now) - int(eur_deily)
            euro_absolut_func = (abs(euro_how_down))
            euro_how_down_fl = (str(0) + '.' + str(euro_absolut_func))
            file.write('€ ' + euro_text + ' = ' + euro_now + '.' + euro_now_ + rub + ' ' + eur_now_down +
                       ' -' + euro_how_down_fl + '\n')

        elif eur_now == eur_deily:
            eur_now_balans = '☯'
            euro_how_balans = int(eur_now) - int(eur_deily)
            euro_how_balans_fl = (str(0) + '.' + str(euro_how_balans))
            file.write('€ ' + euro_text + ' = ' + euro_now + '.' + euro_now_ + rub + ' ' + eur_now_balans
                       + ' ==' + euro_how_balans_fl + '\n')

        file.write('\n' + course + ' ' + currencies + ' на ' + day_daily + '.' + mount_daily + '.' + yuer_daily + '\n')
        file.write('$ ' + dollar_text + ' ' + dollar_usa + ' = ' + dollar_daily + '.' + dollar_daily_ + rub + '\n')
        file.write('€ ' + euro_text + ' = ' + euro_daily + '.' + euro_daily_ + rub)
        file.close()


if __name__ == '__main__':
    finance_parse(base_url, headers)

