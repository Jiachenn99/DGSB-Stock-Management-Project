from django.shortcuts import render

def dashboard(request):
    context = {"dashboard": "active"}
    return render(request, 'main/dashboard.html',context)

def index(request):
    context = {"index": "active"}
    return render(request, 'main/index.html',context)

def login(request):
    context = {"login": "active"}
    return render(request, 'main/login.html',context)

def register(request):
    context = {"register": "active"}
    return render(request, 'main/register.html',context)

def inventory(request):
    context = {"inventory": "active"}
    return render(request, 'main/inventory.html',context)