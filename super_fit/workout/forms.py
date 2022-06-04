from .models import Workout
from django import forms


class WorkourForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['focus', 'types', 'difficult', 'equirment']

    