from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.forms import *
from main.models import *
from main.query_functions import *
import MySQLdb

db = MySQLdb.connect(host="localhost",user="root", db="duriangarden", port = 3306)
results_list = []
headers_list = []

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

    results_list, header_list = get_all_results(Purchasing)

    context = {"purchases": "active",'result': results_list, 'headers_list': header_list}
    return render(request, 'main/purchases.html',context)

def order(request):

    context = {"order": "active"}
    return render(request, 'main/order.html',context)
  
def irrigation(request):

    results_list, header_list = get_all_results(Irrigation)

    context = {"irrigation": "active", 'result': results_list, 'headers_list': header_list}
    return render(request, 'main/irrigation.html',context)

def plantation(request):

    # results_list, header_list = get_all_results(Plantation)

    context = {"plantation": "active"}
    return render(request, 'main/plantation.html',context)

def vehicles(request):

    results_list, header_list = get_all_results(Vehicle) 

    context = {"vehicles": "active",'result': results_list, 'headers_list': header_list}
    return render(request, 'main/vehicles.html',context)

def addItem(request, form_name):
    # Create and update database
    print(form_name)

    if request.method != 'POST':
        form_object = findForm(form_name)  # find the specific form according to the string value passed
        # No data submitted; create a blank form
        form = form_object()
    else:
        print("i have been POST here " + form_name)
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
        'Vehicles' : VehicleForm,
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
    form2 = HerbicideForm
    # form_class = NameForm
    # form = form_class(request.POST or None)
    header_list = []
    results_list = []

    if request.method == "POST":
        if form2.is_valid:
            return HttpResponseRedirect('/thanks/')

    c = db.cursor()
    # addItem(request, Herbicide)

    results_list, header_list = get_all_results(Herbicide)

    # model_fields = Tools._meta.fields
    render_dict = {'result': results_list,'form':form2, 'header_list': header_list}

    return render(request,'main/testing.html',render_dict)


