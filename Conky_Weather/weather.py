#!/usr/bin/python3

import pyowm
import urllib.request
import datetime

times = datetime.datetime.now()

API_key = ''    # API-key https://openweathermap.org/
owm = pyowm.OWM(API_key, language='ru')

sity = 'Лондон'  # you location sity
observation = owm.weather_at_place(sity)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']
observation_list = owm.weather_around_coords(-22.57, -43.12)
atmospheric_pressure = w.get_pressure()['press']
humidity_percentage = w.get_humidity()
speeed = w.get_wind()['speed']
cloud = w.get_clouds()
znak = w.get_weather_icon_url()
icon_znak = urllib.request.urlopen(znak)
file = open('/home/{user}/.config/conky/Conky_NZT/images/icons_weather.png', 'wb')
file.write(icon_znak.read())
file.close()

file = open('/home/{user}/.config/conky/Conky_NZT/Conky_Weather/weather.txt', 'w')     # path to file
file.write('На ' + times.strftime("%d-%m-%Y %H:%M") + '\n')
file.write('В ' + sity + 'е наблюдается:\n')
file.write(w.get_detailed_status() + '. Влажноcть ' + str(humidity_percentage) + '%')
file.write('\nТемпература воздуха: ' + str(temperature) + '℃')
file.write('\nДавление, мм рт.ст: ' + str(atmospheric_pressure) + ' hpa')
file.write('\nСкорость ветра: ' + str(speeed) + 'м\с')
file.close()
