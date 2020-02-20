Conky finance of Central bank Russia Federation

## Screenshots
![Conky](https://github.com/protocolNZT/Conky_NZT/blob/master/images/conky_v0.3.png)

# Install
```ShellSession
$ sudo pip install requests bs4 lxml pyowm
$ mkdir ~/.config/conky/Conky_NZT
$ cd ~/.config/conky/Conky_NZT
$ git clone git@github.com:protocolNZT/Conky_NZT.git
$ mv .conkyrc ~/
```
**Open the directory .config/conky/Conky_NZT/Conky_finance/**
*Open the file "CB_parser_v0.2.py" and change the line for creating the file according to your path:*
```
- file = open('/home/"username"/.config/conky/usdeuro.txt', 'w')    # path to file
```
**Open the directory /.config/conky/Conky_NZT/Conky_Weather/**
*Open the file "weather.py" and change the line for creating the file according to your path 
and specify the API and city:*
```
- API_key = 'you API key'   # API-key https://openweathermap.org/
- sity = 'you location sity'    # you location sity
- file = open('/home/"username"/.config/conky/images/icons_weather.png', 'wb')  # path to file
```
Starting Conky:
```ShellSession
$ conky
```


