from multiprocessing import context
from turtle import color
from django.shortcuts import render
from django.http import HttpResponse
from workouts.models import Workout,Walk
import random
import folium
import geocoder
from . import weather

def index(request):
    warm_up = random.choice(Workout.objects.filter(focus=2).filter(difficult=2 and 3).filter(equirment=2))
    w_full = random.choice(Workout.objects.filter(focus=2).filter(difficult=4).filter(equirment=2).exclude(types=2))
    w_up = random.choice(Workout.objects.filter(focus=3).filter(difficult=4).filter(equirment=2).exclude(types=2))
    w_low = random.choice(Workout.objects.filter(focus=4).filter(difficult=4).filter(equirment=2).exclude(types=2))
    w_abs = random.choice(Workout.objects.filter(focus=5).filter(difficult=4).filter(equirment=2).exclude(types=2))
    m_normal = random.choice(Walk.objects.filter(difficult='normal'))


    m_d = folium.Map(location= (),zoom_start=13,tiles='Stamen Toner')
    m = folium.Map(location= (),zoom_start=14)

    folium.PolyLine(m_normal.route, wieght=6, color='red', opacity=1).add_to(m_d) 
    folium.PolyLine(m_normal.route, wieght=6, color='red', opacity=1).add_to(m)

    m = m._repr_html_()
    m_d = m_d._repr_html_()

    w = weather.weather()

    context = {
        'warm_up' : warm_up,
        'w_full' : w_full,
        'w_up' : w_up,
        'w_low' : w_low,
        'w_abs' : w_abs,
        'm_d' : m_d,
        'm' : m,
        'dis': m_normal.distance,
        'weather' : w,
    }



    '''===================='''
    



    return render(request, template_name='index.html', context=context)


def walks(request):
    location = geocoder.osm('')
    m = folium.Map(location=location.latlng, zoom_start=13, tiles='Stamen Toner')
    folium.Marker(location=location.latlng, popup='Start', icon=folium.Icon(color="red", icon="male", prefix='fa')).add_to(m)
    m = m._repr_html_()
    w = weather.weather()
    context={
        'm' : m,
        'w' : w,
    }
    
    return render(request, template_name='walk.html', context=context)