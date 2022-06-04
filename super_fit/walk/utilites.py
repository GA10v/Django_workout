from django import forms
import random
import geocoder
import polyline
import folium
import requests
from workout.utilits import weather

def get_random(num):
    start = num - 0.01
    stop = num + 0.01
    return random.uniform(start,stop)

    
class WalksForm(forms.Form):
    country = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={"class":'form-control', 'placeholder':'Россия'}))
    city = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":'form-control', 'placeholder':'Москва'}))
    street = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":'form-control', 'placeholder':'Студенческая 33'}))    


class WalkData:
    def __init__(self):
        def_plase = 'Москва Студенческая 33'
        def_location = geocoder.osm(def_plase)
        m = folium.Map(location=def_location.latlng, zoom_start=13, tiles='Stamen Toner')
        folium.Marker(location=def_location.latlng, popup='Start', icon=folium.Icon(color="red", icon="male", prefix='fa')).add_to(m)
        self.def_map = m._repr_html_()
    
    def get_walk(self, plase):
        location = geocoder.osm(plase).latlng

        point1x = get_random(location[0])
        point1y = get_random(location[1])
        point2x = get_random(location[0])
        point2y = get_random(location[1])

        url = f'http://router.project-osrm.org/route/v1/foot/{location[1]},{location[0]};{point1y},{point1x};{point2y},{point2x};{location[1]},{location[0]}?geometries=polyline'

        res = requests.get(url).json()
        routes = polyline.decode(res["routes"][0]["geometry"])
        m = folium.Map(
            location=location,
            zoom_start=14,
            # tiles='Stamen Terrain'
            tiles='Stamen Toner')
        # )
        folium.PolyLine(routes, wieght=6, color='red', opacity=1).add_to(m)
        return m._repr_html_()












        m = folium.Map(location=location, zoom_start=13, tiles='Stamen Toner')










        pass

location = geocoder.osm('Москва Студенческая 33')
m = folium.Map(location=location.latlng, zoom_start=13, tiles='Stamen Toner')
folium.Marker(location=location.latlng, popup='Start', icon=folium.Icon(color="red", icon="male", prefix='fa')).add_to(m)
m = m._repr_html_()
# w = weather.weather()