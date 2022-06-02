from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'lifestyle', 'gender', 'weight', 'task', 'goal', 'age', 'growth']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     try:
    #         kfa ={                               
    #             'Sedentary': 1.0, 
    #             'Active': 1.3,
    #             'Sports':1.5                
    #             }
    #         if self.model.gender == 'Female':
    #             if self.age < 30:
    #                 self.diet = int((0.062 * self.goal + 2.036) * 240 * kfa[self.lifestyle])
    #             elif 31< self.age <60:
    #                 self.diet = int((0.034 * self.goal + 3.538) * 240 * kfa[self.lifestyle])
    #             else:
    #                 self.diet = int((0.038 * self.goal + 2.755) * 240 * kfa[self.lifestyle])
    #         else:
    #             if self.age < 30:
    #                 self.diet = int((0.063 * self.goal + 2.896) * 240 * kfa[self.lifestyle])
    #             elif 31< self.age <60:
    #                 self.diet = int((0.0484 * self.goal + 3.653) * 240 * kfa[self.lifestyle])
    #             else:
    #                 self.diet = int((0.0491 * self.goal + 2.459) * 240 * kfa[self.lifestyle])
            

    #         pass
    #     except ValueError as e:
    #         self.diet = 2000
