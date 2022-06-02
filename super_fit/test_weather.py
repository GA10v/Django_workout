import geocoder
import requests
import fake_useragent
from bs4 import BeautifulSoup





def ia_weather(plase='нижний новгород'):
    location=geocoder.osm(plase).latlng
    lat = location[0]
    lon = location[1]
    url = f'https://yandex.ru/pogoda/nizhny-novgorod?lat={lat}&lon={lon}'
    headers = {'user-agent' : fake_useragent.UserAgent().chrome}
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml').text
    print(soup)



if __name__ == '__main__':
    ia_weather()