from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from main.forms import NameForm, PurchasingForm, OrderForm
from main.models import Purchasing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Q
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
 
# def register(request):
#     context = {"register": "active"}
#     return render(request, 'registration/register.html',context)

def purchases(request):
    #Query variables
    query_results = Purchasing.objects.all()
    query_count = Purchasing.objects.all().count()
    
    #No of Queries
    a = 5
    if request.method == 'POST':
       a = request.POST['drop1']

    #Search query
    query = request.GET.get("q")
    if request.method == 'GET':
        query_results = purchasing_query(query_results, query)

    #Paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(query_results, a)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index -5 else max_index
    page_range = paginator.page_range[start_index:end_index]
     
    context = {
        'query_results': query_results,
        'query_count': query_count,
         'items': items,
         'a': a,
         'pag_template': "main/pagination.html"
         
        }
    return render(request, 'main/purchases.html',context)
  
def irrigation(request, table):

    results, headers = get_all_results(findTable(table))
    cat_list = ['Irrigation']
    context = {'results': results, 'headers': headers, 'cat_list': cat_list, 'label': "irrigation", 'table' : table}

    return render(request, 'main/tables_base.html', context)

def plantation(request, table):
    
    results, headers = get_all_results(findTable(table))
    cat_list = ['Tools', 'Consumables', 'Fungicide']
    context = {'results': results, 'headers': headers, 'cat_list': cat_list, 'label': "plantation", 'table' : table}

    return render(request, 'main/tables_base.html',context)

def vehicle(request, table):
    results, headers = get_all_results(findTable(table))
    cat_list = ['Vehicle', 'Spareparts']
    context = {'results': results, 'headers': headers, 'cat_list': cat_list, 'label': "vehicle", 'table' : table}
    return render(request, 'main/tables_base.html',context)

def order(request):
    context = {"order": "active"}
    form = OrderForm()
    return render(request, 'main/order.html',{'form': form})

def supplier(request):
    
    results, headers= get_all_results(Supplier)
    cat_list = ['Supplier']

    context = {'results': results,'cat_list': cat_list, 'label':"Supplier"}
    return render(request, 'main/supplier.html', context)

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

def userprofile(request):
    context = {"userprofile": "active"}
    return render(request, 'main/userprofile.html',context)
    
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
    
