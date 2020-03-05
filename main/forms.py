from django import forms
from main.models import Supplier
from main.models import Purchasing
from main.models import DropdowmnCategory

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier 
        fields = "__all__"
        

class PurchasingForm(forms.ModelForm):
    class Meta:
        model = Purchasing
        fields = "__all__"



