from django.shortcuts import render, redirect
from .forms import RegisterForm
from account.models import Staff
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from main.decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name = 'staff')
            user.groups.add(group)
            Staff.objects.create(
                user=user,
                name = user.username,
            )
            messages.success(request, 'Account was created for '+ username)
            return redirect("/login")
    else:
        form = RegisterForm()
    
    return render(request,"register/register.html",{"form":form})

