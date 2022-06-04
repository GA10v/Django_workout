from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import random
import folium
import geocoder
from .utilites import WalksForm, WalkData

# Create your views here.


@login_required
def walks(request):
    walk_map = WalkData().def_map
    if request.method == 'POST':
        form = WalksForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                country = data['country']
                city = data['city']
                street = data['street']
                place = f'{country} {city} {street}'
                walk_map = WalkData().get_walk(place)
                context = {
                    'form': form,
                    'map': walk_map
                }
            except Exception as e:
                walk_map = WalkData().def_map
                context = {
                    'form': form,
                    'map': walk_map
                }

    else:
        form = WalksForm()
    context = {
        'form': form,
        'map': walk_map
    }

    return render(request, template_name='walk/walks.html', context=context)
