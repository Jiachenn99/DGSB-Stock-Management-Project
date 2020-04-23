from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Q
from main.forms import *
from main.models import *
from main.query_functions import *
from main.get_data import *
import MySQLdb
from django.http import HttpResponseNotFound

results_list = []
db = MySQLdb.connect(host="localhost",user="root", db="duriangarden", port = 3306)
    
def dashboard(request):
    context = {"dashboard": "active"}
    return render(request, 'main/dashboard.html',context)

def index(request):

    iri_cat_list = get_category_subcat(Irrigation_Tables)
    plant_cat_list = get_category_subcat(Plantation_Tables)

    iri_table = iri_cat_list[0]
    plant_table = plant_cat_list[0]

    context = {"index": "active", 'iri_table_label': iri_table, 'plant_table_label': plant_table}
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
  
def irrigation(request, subcategory):

    category = 'Irrigation_Tables'

    cat_list = get_category_subcat(Irrigation_Tables)
    results = get_all_results(findTable(subcategory))   
    results = get_supplier_name(subcategory, results)

    context = {'results': results,'cat_list': cat_list, 'subcategory' : subcategory, 'category': category}

    return render(request, 'main/tables_base.html', context)

def plantation(request, subcategory):
    
    category = 'Plantation_Tables'

    cat_list = get_category_subcat(Plantation_Tables)
    results= get_all_results(findTable(subcategory))
    results = get_supplier_name(subcategory, results)

    context = {'results': results,'cat_list': cat_list, 'subcategory' : subcategory, 'category':category}

    return render(request, 'main/tables_base.html',context)

def vehicle(request, subcategory):
    results= get_all_results(findTable(subcategory))
    cat_list = ['Vehicle', 'Spareparts']
    context = {'results': results, 'cat_list': cat_list, 'subcategory' : subcategory}
    return render(request, 'main/tables_base.html',context)

def order(request):
    context = {"order": "active"}
    # form = OrderForm(),{'form': form}
    return render(request, 'main/order.html')

def supplier(request):
    
    results= get_all_results(Supplier)
    cat_list = ['Supplier']

    context = {'results': results,'cat_list': cat_list, 'label':"Supplier"}
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
            return redirect(f'/{category}/{subcategory}')

    context = {'form': form, 'form_name': subcategory}
    return render(request, 'main/addItem.html', context)

def userprofile(request):
    context = {"userprofile": "active"}
    return render(request, 'main/userprofile.html',context)
    

def delete_entry(request, pk=None, subcategory=None, category=None):
    if request.method== "POST" and "delete_this" in request.POST:
        table_to_del = findTable(subcategory)
        # for key in switch: 
        #     if subcategory == key:
        #         table_to_del = switch[key]
        #     else:
        #         redirect('/index/')
        #         # Should redirect with an error message back to the page specified by label

        objects = table_to_del.objects.get(pk=pk)
        objects.delete()
        return redirect(f'/{category}/{subcategory}')


def update_entry(request, category=None, subcategory=None, pk=None):
    if request.method == "POST" and "update_this" in request.POST:
        form_to_update = findForm(subcategory)
        model_object = findTable(subcategory)

        # Create a form instance from POST data.
        f = form_to_update(request.POST)

        # Save a new object from the form's data.
        updated_object = f.save()

        # Create a form to edit an existing Article, but use
        # POST data to populate the form.
        a = model_object.objects.get(pk=pk)
        f = form_to_update(request.POST, instance=a)
        f.save()


    return redirect(f'/{category}/{subcategory}')
    
