from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from main.decorators import unauthenticated_user, allowed_users, admin_only


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    #phone = forms.CharField(max_length= 13, help_text='Contact phone number')
    
    class Meta:
        model = User
        fields = ["username","email", "password1","password2"]
    
