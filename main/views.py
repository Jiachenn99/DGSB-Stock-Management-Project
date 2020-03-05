from django.shortcuts import render

def dashboard(request):
    context = {"dashboard": "active"}
    return render(request, 'main/dashboard.html',context)

def index(request):
    context = {"index": "active"}
    return render(request, 'main/index.html',context)

def register(request):
    context = {"register": "active"}
    return render(request, 'register/register.html',context)

def purchases(request):
    context = {"purchases": "active"}
    return render(request, 'main/purchases.html',context)

def order(request):
    context = {"order": "active"}
    return render(request, 'main/order.html',context)
