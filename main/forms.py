from django import forms
from main.models import Supplier
from main.models import Purchasing

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier 
        fields = "__all__"

class PurchasingForm(forms.ModelForm):
    class Meta:
        model = Purchasing
        fields = "__all__"

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
