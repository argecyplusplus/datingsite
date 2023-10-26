from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm (UserCreationForm):
    pass

class MyProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'avatar', 'age', 'gender', 'point_of_searching', 'city', 'social', 'description', 'user')

