from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.forms import *
from main.models import *
from main.query_functions import *
from main.get_data import *
import MySQLdb

results_list = []
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

    results_list = get_all_results(Purchasing)

    context = {"purchases": "active",'result': results_list}
    return render(request, 'main/purchases.html',context)

def order(request):

    context = {"order": "active"}
    return render(request, 'main/order.html',context)
  
def irrigation(request):

    results = get_all_results(Irrigation)
    cat_list = ['Irrigation']
    context = {'results': results, 'cat_list': cat_list, 'label':"Irrigation"}
    return render(request, 'main/irrigation_2.html', context)

def plantation(request):
    
    results = get_plantation()
    cat_list = ['Tools','Fungicide','Consumables']

    context = {'results': results,'cat_list': cat_list, 'label':"Plantation"}
    return render(request, 'main/plantation.html',context)

def vehicle(request):
    context = get_vehicle()
    return render(request, 'main/vehicle.html',context)

def addItem(request, form_name):
    # Create and update database
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
            return redirect('main:{}'.format(form_name.lower()))
    
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

