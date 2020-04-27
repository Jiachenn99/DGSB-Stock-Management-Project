from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from main.decorators import unauthenticated_user, allowed_users, admin_only
from .models import *

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields ='__all__'
        exclude = ['user']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username","email", "password1","password2"]
    
