import json
from tkinter import CASCADE
from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=100, null=True)
    calories = models.PositiveIntegerField(null=True)
    protein = models.FloatField(null=True)
    fats = models.FloatField(null=True)
    carbo = models.FloatField(null=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.name


CATEGORY = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
)

VOLUME = (
    ('gr', 'gr'),
    ('ml', 'ml')
)

# def validate_positive(value):
#     if value < 0:
#         raise ValidationError(f'{value} is not a positsve number', params={'value':value})

'''==========================='''


class Meal(models.Model):
    name = models.ManyToManyField(Food, related_name='d_name')
    calories = models.ManyToManyField(Food, related_name='d_calories')
    protein = models.ManyToManyField(Food, related_name='d_protein')
    fats = models.ManyToManyField(Food, related_name='d_fats')
    carbo = models.ManyToManyField(Food, related_name='d_carbo')
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    date = models.DateField(default=date.today)
    volume = models.CharField(max_length=5, choices=VOLUME, default='gr')
    value = models.FloatField(null=True)
    workout = models.PositiveIntegerField(null=True)


'''=============================='''


class DealyMeal(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    name = models.ManyToManyField(Food, related_name='o_name')
    calories = models.PositiveIntegerField(null=True)
    calories = models.PositiveIntegerField(null=True)
    protein = models.FloatField(null=True)
    fats = models.FloatField(null=True)
    carbo = models.FloatField(null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    date = models.DateField(default=date.today)
    volume = models.CharField(max_length=5, choices=VOLUME, default='gr')
    value = models.FloatField(null=True)


class DealyFit(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200, null=True)
    value = models.PositiveIntegerField(null=True)


def get_food():
    with open('food.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        food = {
            'name': item["name"],
            'category': item["category"],
            'calories': item["call"],
            'protein': item["b"],
            'fats': item["j"],
            'carbo': item["u"],
        }
        Food.objects.create(**food)

def dell():
    a = Food.objects.all()
    for i in a:
        i.delete()

# from diet.models import *
