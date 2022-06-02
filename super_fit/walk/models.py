from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.
class Walk(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    difficult = models.CharField(max_length=10, null=True)
    distance = models.IntegerField(null=True)
    route = models.JSONField(null=True)

class TestWalk(models.Model):
    difficult = models.CharField(max_length=10, null=True)
    distance = models.IntegerField(null=True)
    route = models.JSONField(null=True)



def get_teast_walk():
    with open('base_1500.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for i in data:
        TestWalk.objects.create(**i)

    with open('base_1500.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in data:
        TestWalk.objects.create(**i)

    with open('base_3000.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in data:
        TestWalk.objects.create(**i)


def get_walk(name):
    with open('base_1500.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for i in data:
        user = User.objects.filter(username=name)
        Walk.objects.create(staff=user[0],route=i['route'],distance=i['distance'],difficult=i['difficult'])

    with open('base_2500.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for i in data:
        user = User.objects.filter(username=name)
        Walk.objects.create(staff=user[0],route=i['route'],distance=i['distance'],difficult=i['difficult'])
    
    with open('base_3000.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for i in data:
        user = User.objects.filter(username=name)
        Walk.objects.create(staff=user[0],route=i['route'],distance=i['distance'],difficult=i['difficult'])


def dell():
    a = Walk.objects.all()
    for i in a:
        a.delete()