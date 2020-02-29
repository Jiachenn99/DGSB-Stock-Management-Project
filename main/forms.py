from django import forms
from main.models import Supplier
from main.models import Purchasing
from main.models import DropdowmnCategory

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier 
        fields = "__all__"
        #fields = ("Supplier_ID", "Supplier_Name", "Description")

class PurchasingForm(forms.ModelForm):
    class Meta:
        model = Purchasing
        fields = "__all__"
        #fields = ("Purchasing_ID", "PV_No", "Invoice_No", "Purchasing_Date", "Supplier_ID", "Description")



