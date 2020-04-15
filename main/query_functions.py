from main.models import *
from main.forms import *
from django.db.models import Q, Subquery
from django.apps import apps
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

def model_subclasses(mclass):

    return [m for m in apps.get_models() if issubclass(m, mclass)]