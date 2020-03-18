from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from main.forms import NameForm, PurchasingForm, OrderForm
from main.models import Purchasing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Q
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
    query_results = Purchasing.objects.all()
    query_count = Purchasing.objects.all().count()

    a = 5
    
    #paginator
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


def order(request):
    context = {"order": "active"}
    return render(request, 'main/order.html',context)
  
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



