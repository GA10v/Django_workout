from django import forms
from .models import Food, DealyMeal


class FoodSearch(forms.ModelForm):
    class Meta:
        model = DealyMeal
        fields = ['name', 'value','volume']

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":'form-control', 'placeholder':'яблоко'}))
    value = forms.IntegerField(widget=forms.TextInput(attrs={"class":'form-control', 'placeholder':'100'}))
    volume = forms.Select(attrs={"class":'form-control'})

    # category = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={"class":'form-control', 'placeholder':'Россия'}))

    