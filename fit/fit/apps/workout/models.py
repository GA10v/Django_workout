from django.db import models


class Workout(models.Model):
    name = models.CharField('name', max_length=100)
    focus = models.CharField('focus', max_length=50)
    types = models.CharField('type', max_length=50)
    difficult = models.CharField('difficult', max_length=20)
    equirment = models.CharField('equirement', max_length=50)
    icon = models.CharField('img intro', max_length=200)
    img = models.CharField('img link', max_length=200)
    muscles = models.CharField('img muscles', max_length=200)
