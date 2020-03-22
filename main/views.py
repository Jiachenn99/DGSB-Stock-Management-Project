from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.forms import *
from main.models import *
from main.query_functions import *
from main.get_data import *
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

def purchases(request):
    context = {"purchases": "active"}
    return render(request, 'main/purchases.html',context)

def order(request):
    context = {"order": "active"}
    return render(request, 'main/order.html',context)
  
def irrigation(request):
    context = get_irrigation()
    return render(request, 'main/irrigation.html', context)

def plantation(request):
    context = get_plantation()
    return render(request, 'main/plantation.html',context)

def vehicle(request):
    context = get_vehicle()
    return render(request, 'main/vehicle.html',context)

def addItem(request, form_name):
    
    print(form_name)

    if request.method != 'POST':
        form_object = findForm(form_name)  # find the specific form according to the string value passed
        # No data submitted; create a blank form
        form = form_object()
    else:
        form_object = findForm(form_name)  # find the specific form according to the string value passed
        # POST data submitted; process data
        form = form_object(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    
    context = {'form': form, 'form_name': form_name}
    return render(request, 'main/addItem.html', context)

def findForm(form_type):
    switch={
        'Supplier' : SupplierForm,
        'Purchasing' : PurchasingForm,
        'Name' : NameForm,
        'Tools' : ToolsForm,
        'Irrigation' : IrrigationForm,
        'Spareparts' : SparepartsForm,
        'Vehicle' : VehicleForm,
        'Stationery' : StationeryForm,
        'Consumables' : ConsumablesForm,
        'Fungicide' : FungicideForm,
        'Fertilizer' : FertilizerForm,
        'Surfacetant' : SurfacetantForm,
        'Herbicide' : HerbicideForm,
        'Pesticide' : PesticideForm,
    }
    return switch.get(form_type)


def get_name(request):

    # Initializing the form
    form2 = PurchasingForm
    # form_class = NameForm
    # form = form_class(request.POST or None)

    if request.method == "POST":
        if form2.is_valid:
            return HttpResponseRedirect('/thanks/')

    c = db.cursor()
    # addItem(request, Herbicide)

    c.execute("""SELECT * FROM herbicide""")

    r2 = c.fetchall()

    # r3 = isinstance(r2, tuple)

    some_dict = {'result': r2,'form':form2}

    return render(request,'main/testing.html',some_dict)
