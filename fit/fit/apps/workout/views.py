from django.shortcuts import render
from django.http import HttpResponse

def workout(request):
    return HttpResponse('workouts')

