from main.models import *
from main.query_functions import *


def get_irrigation():
    results_Irrigation, headers_Irrigation = get_all_results(Irrigation)
    context = {"irrigation": "active", 'results_Irrigation': results_Irrigation, 'headers_Irrigation': headers_Irrigation}

    return context

def get_plantation():
    results_Tools = get_all_results(Tools)
    results_Consumables = get_all_results(Consumables)
    results_Fungicide = get_all_results(Fungicide)
    context = {"plantation": "active", 
    'results_Tools': results_Tools, 
    'results_Consumables': results_Consumables, 
    'results_Fungicide': results_Fungicide,
    }

    return context

def get_vehicle():
    results_Vehicle, headers_Vehicle = get_all_results(Vehicle)
    results_Spareparts, headers_Spareparts = get_all_results(Spareparts)
    context = {"vehicle": "active", 
    'results_Vehicle': results_Vehicle, 'headers_Vehicle': headers_Vehicle,
    'results_Spareparts': results_Spareparts, 'headers_Spareparts': headers_Spareparts,
    }

    return context

def get_supplier():
    results_Supplier = get_all_results(Supplier)
    context = {"supplier": "active", 'results_Supplier': results_Supplier}

    return context

