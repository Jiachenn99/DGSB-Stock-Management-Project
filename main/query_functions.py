from main.models import *
from main.forms import *
from django.db.models import Q
from functools import reduce
import operator

# Focusing on CRUD
# C - Create
# R - Retrieve
# U - Update
# D - Delete

# Retrieve
def get_all_results(table):
    '''
    Retrieves all rows of a particular table

    Args:
    table: name of database table

    Returns: 
    return_list: QuerySet object of dicts of object, with dict being {'field_name': value...}
    '''

    return_list = table.objects.all().values()

    return return_list

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
    query = table.objects.filter(reduce(operator.and_, (Q(**d) for d in [dict([i]) for i in condition.items()])))

    table.objects.delete(query)

    return query

def delete_multiple_from_table(table, condition):
    '''
    Args:
    condition: list of dicts

    '''
    return 0

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