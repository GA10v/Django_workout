from django.shortcuts import render
from django.http import HttpResponse
from .models import Workout

import random

def workout(request):
    first_workout = Workout.objects.all()[1]
    workouts = Workout.objects.all()[2:7]
    return render(request, 'workout/index.html', {'first_workout':first_workout,'workouts':workouts, 'title':'title'})


def get_wk(request, focus1):
    # wk = Workout.objects.filter( in focus)
    pass



# def workout(request):
#     a = Workout.objects.all()
#     warm_up = []
#     for i in a:
#         if 'easy' in i.difficult\
#             or 'easy' in i.difficult\
#             and 'none' in i.equirment :
#             warm_up.append(i.icon)
#     return render(request, 'workout/1.html', {'test':random.choice(warm_up)})


