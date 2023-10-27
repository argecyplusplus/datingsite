from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User


class RegisterForm (UserCreationForm):
    pass

class MyProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'avatar', 'age', 'gender', 'point_of_searching', 'city', 'social', 'description', 'user', 'age_search_min', 'age_search_max')
