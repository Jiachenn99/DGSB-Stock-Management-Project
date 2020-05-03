# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm
from account.models import Staff
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from main.decorators import unauthenticated_user, allowed_users, admin_only
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.utils.translation import ugettext as _

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group, created = Group.objects.get_or_create(name = 'staff')
            user.groups.add(group)
            Staff.objects.create(
                user=user,
                name = user.username,
                email = user.email,
            )
            messages.success(request, 'Account was created for '+ username)
            return redirect("/login")
    else:
        form = RegisterForm()
    
    return render(request,"registration/register.html",{"form":form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {
        'form': form
    })