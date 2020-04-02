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
  
def irrigation(request, table):

    results, headers = get_all_results(findTable(table))
    cat_list = ['Irrigation']
    context = {'results': results, 'headers': headers, 'cat_list': cat_list, 'table': table}

    return render(request, 'main/irrigation.html', context)

def plantation(request, table):
    
    results, headers = get_all_results(findTable(table))
    cat_list = ['Tools', 'Consumables', 'Fungicide']
    context = {'results': results, 'headers': headers, 'cat_list': cat_list, 'table': table}

    return render(request, 'main/plantation.html',context)

def vehicle(request, table):

    results, headers = get_all_results(findTable(table))
    cat_list = ['Vehicle', 'Spareparts']
    context = {'results': results, 'headers': headers, 'cat_list': cat_list, 'table': table}

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

def findTable(table):
    switch={
        'Supplier' : Supplier,
        'Purchasing' : Purchasing,
        'Tools' : Tools,
        'Irrigation' : Irrigation,
        'Spareparts' : Spareparts,
        'Vehicle' : Vehicle,
        'Stationery' : Stationery,
        'Consumables' : Consumables,
        'Fungicide' : Fungicide,
        'Fertilizer' : Fertilizer,
        'Surfacetant' : Surfacetant,
        'Herbicide' : Herbicide,
        'Pesticide' : Pesticide,
    }
    return switch.get(table)

def delete_entry(request, pk=None, object=None, label=None):
    switch={
        'Supplier' : Supplier,
        'Purchasing' : Purchasing,
        'Tools' : Tools,
        'Irrigation' : Irrigation,
        'Spareparts' : Spareparts,
        'Vehicle' : Vehicle,
        'Stationery' : Stationery,
        'Consumables' : Consumables,
        'Fungicide' : Fungicide,
        'Fertilizer' : Fertilizer,
        'Surfacetant' : Surfacetant,
        'Herbicide' : Herbicide,
        'Pesticide' : Pesticide,
    }

    if request.method=="POST" and "delete_this" in request.POST:
        for key in switch: 
            if label == key:
                table_to_del = switch[key]
            else:
                redirect('/index/')
                # Should redirect with an error message back to the page specified by label

        objects = table_to_del.objects.get(pk=pk)
        print(f'The soon to be deleted object is: {objects.pk}\n')
        objects.delete()
        return redirect('/irrigation/')
    else:
        print("Big sad")
    