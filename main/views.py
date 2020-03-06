from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.forms import *
from main.models import *
import MySQLdb

db = MySQLdb.connect(host="localhost",user="root", db="duriangarden", port = 3306)


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

def addItem(request):
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = ToolsForm()
    else:
        # POST data submitted; process data
        form = ToolsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    
    context = {'form': form}
    return render(request, 'main/addItem.html', context)


def get_name(request):

    # Initializing the form
    form2 = PurchasingForm
    # form_class = NameForm
    # form = form_class(request.POST or None)

    if request.method == "POST":
        if form2.is_valid:
            return HttpResponseRedirect('/thanks/')

    c = db.cursor()

    c.execute("""SELECT * FROM herbicide""")

    r2 = c.fetchall()

    # r3 = isinstance(r2, tuple)

    some_dict = {'result': r2,'form':form2}

    return render(request,'main/testing.html',some_dict)
