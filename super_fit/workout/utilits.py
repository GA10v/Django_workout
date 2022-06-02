import random
from .models import Workout
from walk.models import Walk, TestWalk
import geocoder
import folium
import requests
import fake_useragent
from bs4 import BeautifulSoup
from .config import WEATHER_KEY


def weather(plase='нижний новгород'):
    API_key = WEATHER_KEY #take it on https://openweathermap.org/api
    location=geocoder.osm(plase).latlng
    lat = location[0]
    lon = location[1]
    
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric&lang=ru'
    headers = {'user-agent' : fake_useragent.UserAgent().random}

    data = requests.get(url=url, headers=headers).json()

    weather = {
        'main' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'temp' : data['main']['temp'],
        'feels' : data['main']['feels_like'],
        'wind' : data['wind']['speed'],
    }
    return weather


def ia_weather(plase='нижний новгород'):
    location=geocoder.osm(plase).latlng
    lat = location[0]
    lon = location[1]
    url = f'https://yandex.ru/pogoda/nizhny-novgorod?lat={lat}&lon={lon}'
    headers = {'user-agent' : fake_useragent.UserAgent().random}
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml').text
    print(url)



# lat=56.3264816&lon=44.0051395

56.3264816, 44.0051395

class DailyTaskDemo:
    def __init__(self):
        self.warm_up = random.choice(Workout.objects.filter(focus=2).filter(difficult=2 and 3).filter(equirment=2))
        self.w_full = random.choice(Workout.objects.filter(focus=2).filter(difficult=4).filter(equirment=2).exclude(types=2))
        self.w_up = random.choice(Workout.objects.filter(focus=3).filter(difficult=4).filter(equirment=2).exclude(types=2))
        self.w_low = random.choice(Workout.objects.filter(focus=4).filter(difficult=4).filter(equirment=2).exclude(types=2))
        self.w_abs = random.choice(Workout.objects.filter(focus=5).filter(difficult=4).filter(equirment=2).exclude(types=2))

        m_normal = random.choice(TestWalk.objects.filter(difficult='normal'))
        m_d = folium.Map(location= (56.338388, 43.936423),zoom_start=13,tiles='Stamen Toner')
        m = folium.Map(location= (56.338388, 43.936423),zoom_start=14)

        folium.PolyLine(m_normal.route, wieght=6, color='red', opacity=1).add_to(m_d) 
        folium.PolyLine(m_normal.route, wieght=6, color='red', opacity=1).add_to(m)

        self.m = m._repr_html_()
        self.m_d = m_d._repr_html_()

        self.weather = weather()

