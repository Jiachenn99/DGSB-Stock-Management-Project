from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.db.models import F
from main.forms import *
from main.models import *
from main.query_functions import *
from main.get_data import *
from durianGarden.settings import EMAIL_HOST_USER
import MySQLdb
from django.http import HttpResponseNotFound
import datetime

results_list = []
db = MySQLdb.connect(host="localhost",user="root", db="duriangarden", port = 3306)
    
def dashboard(request):
    total_items = 0

    count1= Spareparts.objects.all().count()
    count2= Tools.objects.all().count()
    count3= Stationery.objects.all().count()
    count4= Consumables.objects.all().count()
    count5= Fungicide.objects.all().count()
    count6= Fertilizer.objects.all().count()
    count7= Surfacetant.objects.all().count()
    count8= Herbicide.objects.all().count()
    count9= Pesticide.objects.all().count()
    count10= Irrigation.objects.all().count()
    
    total_items = count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 + count10

    item_lowStock = 0
    low1 = Tools.objects.all().filter(quantity__lte=F('threshold')).count()
    low2 = Consumables.objects.all().filter(quantity__lte=F('threshold')).count()
    low3 = Fungicide.objects.all().filter(quantity__lte=F('threshold')).count()
    low4 = Fertilizer.objects.all().filter(quantity__lte=F('threshold')).count()
    low5 = Surfacetant.objects.all().filter(quantity__lte=F('threshold')).count()
    low6 = Herbicide.objects.all().filter(quantity__lte=F('threshold')).count()
    low7 = Pesticide.objects.all().filter(quantity__lte=F('threshold')).count()
    low8 = Irrigation.objects.all().filter(quantity__lte=F('threshold')).count()

    item_lowStock = low1 + low2 + low3 + low4 + low5 + low6 + low7 + low8 
    context = {
        "dashboard": "active",
        'total_items': total_items,
        'item_lowStock': item_lowStock
    }
    return render(request, 'main/dashboard.html',context)

def index(request):

    iri_cat_list = get_category_subcat(Irrigation_Tables)
    plant_cat_list = get_category_subcat(Plantation_Tables)
    vehicle_cat_list  = get_category_subcat(Vehicle_Tables)

    iri_table = iri_cat_list[0]
    plant_table = plant_cat_list[0]
    vehicle_table = vehicle_cat_list[0]

    context = {"index": "active", 'iri_table_label': iri_table, 'plant_table_label': plant_table, 'vehicle_table_label': vehicle_table}
    return render(request, 'main/index.html',context)
 
# def register(request):
#     context = {"register": "active"}
#     return render(request, 'registration/register.html',context)

def purchasing(request):
    category = 'purchasing'
    subcategory = 'Purchasing'
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
    
    results = get_all_results(Purchasing)
    cat_list = ['Purchasing']

    context = {
        'query_results': query_results,
        'query_count': query_count,
         'items': items,
         'a': a,
         'pag_template': "main/pagination.html",
         'results': results,
         'cat_list': cat_list, 
         'label':"Purchasing"
         , 'subcategory' : subcategory, 'category': category
         
        }
    return render(request, 'main/purchasing.html',context)
  
def irrigation(request, subcategory):

    category = 'Irrigation_Tables'

    cat_list = get_category_subcat(Irrigation_Tables)
    results = get_all_results(findTable(subcategory))   
    results = get_supplier_name(subcategory, results)

    context = {'results': results,'cat_list': cat_list, 'subcategory': subcategory, 'category': category}

    return render(request, 'main/tables_base.html', context)

def plantation(request, subcategory):
    
    category = 'Plantation_Tables'

    cat_list = get_category_subcat(Plantation_Tables)
    results = get_all_results(findTable(subcategory))
    results = get_supplier_name(subcategory, results)

    context = {'results': results,'cat_list': cat_list, 'subcategory': subcategory, 'category': category}

    return render(request, 'main/tables_base.html',context)

def vehicle(request, subcategory):

    category = 'Vehicle_Tables'

    cat_list = get_category_subcat(Vehicle_Tables)
    results = get_all_results(findTable(subcategory))
    if subcategory == 'Spareparts':
        results = get_supplier_name(subcategory, results)
    
    context = {'results': results, 'cat_list': cat_list, 'subcategory': subcategory, 'category': category}
    return render(request, 'main/tables_base.html',context)

def orderView(request):
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            subject = "DurianGarden order on " + str(datetime.date.today())
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, EMAIL_HOST_USER , [email], fail_silently = False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('main:success')
    return render(request, 'main/order.html',{'form': form})

def successView(request):
    
    return HttpResponse('Success! Thank you for your order.')

def supplier(request):
    category = 'supplier'
    subcategory = 'Supplier'
    results= get_all_results(Supplier)
    cat_list = ['Supplier']

    context = {'results': results,'cat_list': cat_list, 'label':"Supplier", 'subcategory' : subcategory, 'category': category}
    return render(request, 'main/supplier.html', context)

def addItem(request, category, subcategory):
    # Create and update database
    print('dsadsaads') 

    if request.method != 'POST':
        form_object = findForm(subcategory)  # find the specific form according to the string value passed
        # No data submitted; create a blank form
        form = form_object()
    else:
        form_object = findForm(subcategory)  # find the specific form according to the string value passed
        # POST data submitted; process data
        form = form_object(data=request.POST)   
        if form.is_valid():
            form.save()
            if subcategory == 'Purchasing' or subcategory == 'Supplier':
                return redirect(f'/{category}/')
            else:
                return redirect(f'/{category}/{subcategory}')

    context = {'form': form, 'form_name': subcategory}
    return render(request, 'main/addItem.html', context)

def findForm(form_type):
    switch={
        'Supplier' :SupplierForm,
        'Purchasing' :PurchasingForm,
        'Tools' :ToolsForm,
        'Irrigation' :IrrigationForm,
        'Spareparts' :SparepartsForm,
        'Vehicle' :VehicleForm,
        'Stationery' :StationeryForm,
        'Consumables' :ConsumablesForm,
        'Fungicide' :FungicideForm,
        'Fertilizer' :FertilizerForm,
        'Surfacetant' :SurfacetantForm,
        'Herbicide' :HerbicideForm,
        'Pesticide' :PesticideForm,
    }
    return switch.get(form_type)

def userprofile(request):
    context = {"userprofile": "active"}
    return render(request, 'main/userprofile.html',context)
    

def delete_entry(request, pk=None, subcategory=None, category=None):
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

    if request.method== "POST" and "delete_this" in request.POST:
        for key in switch: 
            if subcategory == key:
                table_to_del = switch[key]
            else:
                redirect('/index/')
                # Should redirect with an error message back to the page specified by label

        objects = table_to_del.objects.get(pk=pk)
        print(f'The soon to be deleted object is: {objects.pk}\n')
        objects.delete()
        return redirect(f'/{category}/{subcategory}')

    else:
        print("Big sad")

def update_entry(request, subcategory = None):



    return redirect(f'/{category}/{subcategory}')