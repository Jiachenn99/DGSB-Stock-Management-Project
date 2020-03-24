from main.models import *
from main.forms import *

# Focusing on CRUD
# C - Create
# R - Retrieve
# U - Update
# D - Delete

# Create
def add():


    return 0 

# Retrieve
def get_all_results(table, **field_with_value):
    header_list = []
    # List of dictionaries of key:value pairs of column: value
    results_list = table.objects.values()

    # Get table headers
    for dicts in results_list:
        for keys in dicts.keys():
            header_list.append(keys)
            continue
        break

    return results_list, header_list


def delete_from_table(table, **condition):


    return 0
