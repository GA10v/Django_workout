from django.db import models
from datetime import date



# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=100, null=True)
    calories = models.PositiveIntegerField(null=True)
    protein = models.FloatField(null=True)
    fats = models.FloatField(null=True)
    carbo = models.FloatField(null=True)

CATEGORY=(
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
)

VOLUME = (
    ('gr','gr'),
    ('ml', 'ml')
)

# def validate_positive(value):
#     if value < 0:
#         raise ValidationError(f'{value} is not a positsve number', params={'value':value})


class Meal(models.Model):
    name = models.ManyToManyField(Food, related_name='d_name')
    calories = models.ManyToManyField(Food, related_name='d_calories')
    protein = models.ManyToManyField(Food, related_name='d_protein')
    fats = models.ManyToManyField(Food, related_name='d_fats')
    carbo =models.ManyToManyField(Food, related_name='d_carbo')
    category = models.CharField(max_length=100,choices=CATEGORY, null=True)
    date = models.DateField(default=date.today)
    volume = models.CharField(max_length=5,choices=VOLUME, default='gr')
    value = models.FloatField(null=True)
    workout = models.PositiveIntegerField(null=True)