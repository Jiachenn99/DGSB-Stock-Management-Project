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
    Retrieves all rows and headers of a particular table

    Args:
    table: name of database table

    Returns: 
    results_list: QuerySet object of dicts of object, with dict being {'field_name': value...}
    headers_list: A dictionary containing all keys (headers) of current table
    '''

    results_list = table.objects.all().values()
    headers_list = table.objects.all().values()[0].keys()

    return results_list, headers_list

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
