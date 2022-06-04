from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from workout.models import Workout
from .utilits import DailyTaskDemo
from diet.utilits import FoodDemo
from diet.models import Food
from .forms import WorkourForm
from django.core.paginator import Paginator
import json

# Create your views here.


def index_demo(request):
    daily = DailyTaskDemo()
    food = FoodDemo().all_food
    '''========================'''

    if request.is_ajax():
        q = request.GET.get('term', '')
        food = Food.objects.filter(name__icontains=q)
        results = []
        for fo in food:
            food_json = {}
            food_json = fo.name + "," + fo.category
            results.append(food_json)
        data = json.dumps(results)

    '''======================'''
    context = {
        'daily': daily,
        'food': food
    }
    return render(request, template_name='home/index_demo.html', context=context)


@login_required
def index(request):
    daily = DailyTaskDemo()
    context = {
        'daily': daily
    }
    return render(request, template_name='home/index_demo.html', context=context)


@login_required
def w_index(request):
    work = Workout.objects.all()  
    paginator = Paginator(work, 8)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    if request.method == 'POST':
        form = WorkourForm(request.POST)
        focus = request.POST['focus']
        types = request.POST['types']
        difficult = request.POST['difficult']
        equirment = request.POST['equirment']
        work = Workout.objects.all()
        if focus != '1':
            work = work.filter(focus=focus)
            print(work.count())
        if types != '1':
            work = work.filter(focus=types)
            print(work.count())
        if difficult != '1':
            work = work.filter(focus=difficult)
            print(work.count())
        if equirment != '1':
            work = work.filter(focus=equirment)
            print(work.count())
        
        paginator = Paginator(work, 8)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        
        context = {
            'form': form,
            'workout': work,
            'page': page_obj,
        }

    else:        
        form = WorkourForm()
        context = {
            'form': form,
            'workout': work,
            'page': page_obj,
        }
    return render(request, template_name='workout/index.html', context=context)
