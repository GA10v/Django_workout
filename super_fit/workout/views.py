from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utilits import DailyTaskDemo

# Create your views here.
def index_demo(request):
    daily = DailyTaskDemo()
    context = {
        'daily' : daily
    }
    return render(request, template_name='home/index_demo.html', context=context)


@login_required
def index(request):
    daily = DailyTaskDemo()
    context = {
        'daily' : daily
    }
    return render(request, template_name='home/index_demo.html', context=context)


@login_required
def w_index(request):
    context = {}
    return render(request, template_name='workout/index.html', context=context)

