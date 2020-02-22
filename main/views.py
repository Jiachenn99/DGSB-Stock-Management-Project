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

def irrigation(request):
    context = {"irrigation": "active"}
    return render(request, 'main/irrigation.html',context)

def plantation(request):
    context = {"plantation": "active"}
    return render(request, 'main/plantation.html',context)

def vehicles(request):
    context = {"vehicles": "active"}
    return render(request, 'main/vehicles.html',context)