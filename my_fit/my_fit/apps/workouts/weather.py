import requests
import geocoder
import fake_useragent
from config import WEATHER_KEY

def weather(location=geocoder.osm('').latlng):
    lat = location[0]
    lon = location[1]

    API_key = WEATHER_KEY #take it on https://openweathermap.org/api
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric&lang=ru'
    headers = {'user-agent' : fake_useragent.UserAgent().random}

    data = requests.get(url=url, headers=headers).json()
    # print(data)

    # with open('test_weather.json', 'w', encoding='utf-8') as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)
    weather = {
        'main' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'temp' : data['main']['temp'],
        'feels' : data['main']['feels_like'],
        'wind' : data['wind']['speed'],
    }
    return weather



