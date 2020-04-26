from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields ='__all__'
        exclude = ['user']