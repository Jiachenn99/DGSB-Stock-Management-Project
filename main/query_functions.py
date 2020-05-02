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

def get_results_count(table):

    results_count = table.objects.all().values().count()

    return results_count

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

def purchasing_query(results, query):
    if query:
        results = results.filter(
            Q(pv_no__iexact=query) |
            Q(invoice_no__iexact=query) |
            Q(purchasing_date__icontains=query) |
            Q(description__icontains=query) 
            
            ).distinct()
    return results

def supplier_query(results, query):
    if query:
        results = results.filter(
            Q(supplier_name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(email__icontains=query) |
            Q(description__icontains=query) 
            ).distinct()
    return results

def irrigation_query(results, query):
    if query:
        results = results.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(supplier__supplier_name__icontains=query) 
            ).distinct()
    return results

def plantation_query(results, query):
    if query:
        results = results.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(supplier__supplier_name__icontains=query) 
            ).distinct()
    return results

def vehicle_query(results, query):
    if query:
        results = results.filter(
            Q(vehicle_type__icontains=query) |
            Q(vehicle_name__icontains=query) |
            Q(vehicle_number_plate__icontains=query) |
            Q(vehicle_owner__icontains=query) 
            ).distinct()
    return results

def spareparts_query(results, query):
    if query:
        results = results.filter(
            Q(name__icontains=query) |
            Q(vehicle_assigned__icontains=query) |
            Q(supplier__supplier_name__icontains=query) 
            ).distinct()
    return results
    
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
            if 'id' in dicts.keys():
                model_object = subcategory.objects.get(pk = dicts['id'])
                if 'supplier_id' in dicts.keys():
                    supplier_name = model_object.supplier
                    dicts['supplier_id'] = supplier_name
                if 'purchasing_id' in dicts.keys():
                    pv_no = model_object.purchasing
                    dicts['purchasing_id'] = pv_no
            
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
    Stationery_low = Stationery.objects.all().filter(quantity__lte=F('threshold'))
    Consumables_low = Consumables.objects.all().filter(quantity__lte=F('threshold'))
    Fungicide_low = Fungicide.objects.all().filter(quantity__lte=F('threshold'))
    Fertilizer_low = Fertilizer.objects.all().filter(quantity__lte=F('threshold'))
    Surfacetant_low = Surfacetant.objects.all().filter(quantity__lte=F('threshold'))
    Herbicide_low = Herbicide.objects.all().filter(quantity__lte=F('threshold'))
    Pesticide_low = Pesticide.objects.all().filter(quantity__lte=F('threshold'))
    Spartparts_low = Spareparts.objects.all().filter(quantity__lte=F('threshold'))

    Irrigation_low = get_supplier_name('Irrigation', Irrigation_low.values())
    Tools_low = get_supplier_name('Tools', Tools_low.values())
    Stationery_low = get_supplier_name('Stationery', Stationery_low.values())
    Consumables_low = get_supplier_name('Consumables', Consumables_low.values())
    Fungicide_low = get_supplier_name('Fungicide', Fungicide_low.values())
    Fertilizer_low = get_supplier_name('Fertilizer', Fertilizer_low.values())
    Surfacetant_low = get_supplier_name('Surfacetant', Surfacetant_low.values())
    Herbicide_low = get_supplier_name('Herbicide', Herbicide_low.values())
    Pesticide_low = get_supplier_name('Pesticide', Pesticide_low.values())
    Spartparts_low = get_supplier_name('Spareparts', Spartparts_low.values())


    if Irrigation_low.exists():
        Irrigation_low_list = [Irrigation_low]
    else:
        Irrigation_low_list = []
    
    if Tools_low.exists() or Consumables_low.exists() or Stationery_low.exists() or Fungicide_low.exists() or Fertilizer_low.exists() or Surfacetant_low.exists() or Herbicide_low.exists() or Pesticide_low.exists():
        Plantation_low_list = [Tools_low, Consumables_low, Stationery_low, Fungicide_low, Fertilizer_low, Surfacetant_low, Herbicide_low, Pesticide_low]
    else:
        Plantation_low_list = []

    if Spartparts_low.exists():
        Spartparts_low_list = [Spartparts_low]
    else:
        Spartparts_low_list = []

    return Irrigation_low_list, Plantation_low_list, Spartparts_low_list