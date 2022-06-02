from django.db import models
from django.contrib.auth.models import User
from .validations import validate_positive


TASK = (
    ('get slim', 'get slim'),
    ('get save', 'get save'),
    ('get save','get grow'),
)
LIFESTYLE = (
    ('Sedentary', 'Sedentary'),
    ('Active','Active'),
    ('Sports', 'Sports'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=50, null=True)
    weight = models.FloatField(null=True, validators=[validate_positive], error_messages={'required': 'Please enter positive number'})
    task = models.CharField(max_length=10, choices=TASK, null=True)    
    goal = models.FloatField(null=True, validators=[validate_positive], error_messages={'required': 'Please enter positive number'})
    lifestyle = models.CharField(max_length=15, choices=LIFESTYLE, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank='Male')
    diet = models.PositiveIntegerField(null=True)
    age = models.PositiveIntegerField(null=True)
    growth = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name} - {self.task}'
