from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from main.forms import NameForm, PurchasingForm, OrderForm
from main.models import Purchasing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Q
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
    if query:
        query_results = query_results.filter(
            Q(purchasing_id__icontains=query) |
            Q(pv_no__icontains=query) |
            Q(invoice_no__icontains=query) |
            Q(purchasing_date__icontains=query) |
            Q(description__icontains=query) |
            Q(supplier__supplier_name__icontains=query) 
            ).distinct()

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
         
        }
    return render(request, 'main/purchases.html',context)
  
def irrigation(request):
    context = {"irrigation": "active"}
    return render(request, 'main/irrigation.html',context)

def plantation(request):
    context = {"plantation": "active"}
    return render(request, 'main/plantation.html',context)

def vehicles(request):
    context = {"vehicles": "active"}
    return render(request, 'main/vehicles.html',context)
    
def order(request):
    context = {"order": "active"}
    form = OrderForm()
   
    return render(request, 'main/order.html',{'form': form})

def addItem(request, form_name):
    
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

def userprofile(request):
    context = {"userprofile": "active"}
    return render(request, 'main/userprofile.html',context)
