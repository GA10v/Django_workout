from django.shortcuts import render
from django.http import HttpResponse
from .models import Workout

def workout(request):
    first_workout = Workout.objects.all()[1]
    workouts = Workout.objects.all()[2:7]
    return render(request, 'workout/index.html', {'first_workout':first_workout,'workouts':workouts, 'title':'title'})

