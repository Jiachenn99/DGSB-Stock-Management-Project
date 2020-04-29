from main.models import *
from main.forms import *
from functools import reduce
from django.apps import apps
from django.db.models import Q, Subquery,F
import operator

# Focusing on CRUD
# C - Create
# R - Retrieve
# U - Update
# D - Delete

# Retrieve
def get_all_results(table):
    '''
    Retrieves all rows and headers of a particular table

    Args:
    table: name of database table

    Returns: 
    results_list: QuerySet object of dicts of object, with dict being {'field_name': value...}
    '''

    results_list = table.objects.all().values()

    return results_list
# Delete
def delete_from_table(table, condition, count=None):
    '''
    Deletes a single object matching the filter

    Args:
    table = name of database table
    condition = dictionary of items user wants to delete. eg. {'id': 4...}

    Returns:
    None
    '''
    to_del_table = findTable(table)

    query = to_del_table.objects.filter(reduce(operator.and_, (Q(**d) for d in [dict([i]) for i in condition.items()])))

    to_del_table.objects.delete(query)

    return query

def purchasing_query(query_results, query):
    if query:
        query_results = query_results.filter(
            Q(purchasing_id__icontains=query) |
            Q(pv_no__icontains=query) |
            Q(invoice_no__icontains=query) |
            Q(purchasing_date__icontains=query) |
            Q(description__icontains=query) |
            Q(supplier__supplier_name__icontains=query) 
            ).distinct()
    return query_results

def model_subclasses(mclass):

    return [m for m in apps.get_models() if issubclass(m, mclass)]


def get_category_subcat(parent_class):

    categories_list = [i._meta.model.__name__ for i in model_subclasses(parent_class)]

    return categories_list

def get_supplier_name(subcategory, some_queryset):

    temp_dict = {}
    temp_list = []

    subcategory = findTable(subcategory)

    # If empty
    if not some_queryset:
        pass

    else:
        for dicts in some_queryset:
            model_object = subcategory.objects.get(pk = dicts['id'])
            supplier_name = model_object.purchasing.supplier.supplier_name
            del[dicts['purchasing_id']]
            dicts['supplier_name'] = supplier_name
            
    return some_queryset        

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

def get_low_stock_results():

    # get all querysets that have quantity LTE threshold
    Irrigation_low = Irrigation.objects.all().filter(quantity__lte=F('threshold'))
    Tools_low = Tools.objects.all().filter(quantity__lte=F('threshold'))
    Consumables_low = Consumables.objects.all().filter(quantity__lte=F('threshold'))
    Fungicide_low = Fungicide.objects.all().filter(quantity__lte=F('threshold'))
    Fertilizer_low = Fertilizer.objects.all().filter(quantity__lte=F('threshold'))
    Surfacetant_low = Surfacetant.objects.all().filter(quantity__lte=F('threshold'))
    Herbicide_low = Herbicide.objects.all().filter(quantity__lte=F('threshold'))
    Pesticide_low = Pesticide.objects.all().filter(quantity__lte=F('threshold'))

    Irrigation_low_list = [Irrigation_low]
    Plantation_low_list = [Tools_low, Consumables_low, Fungicide_low, Fertilizer_low, Surfacetant_low, Herbicide_low, Pesticide_low]

    return Irrigation_low_list, Plantation_low_list