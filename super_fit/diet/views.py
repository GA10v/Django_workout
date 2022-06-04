from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from .forms import FoodSearch
from . models import Food

# Create your views here.


def diet(request):
    if request.method == 'POST':
        # q
        form = FoodSearch(request.POST)
        food = request.POST['name']
        result = Food.objects.filter(name__contains=food)

        # food = Food.objects.filter(name__i)
        context = {
            'form': form,
            'food': result,
        }
        return render(request, template_name='diet/diet_index.html', context=context)

    else:
        form = FoodSearch()
    context = {
        'form': form,
    }
    return render(request, template_name='diet/diet_index.html', context=context)
