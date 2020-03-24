from django import forms
from main.models import *

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

class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        fields = "__all__"

class IrrigationForm(forms.ModelForm):
    class Meta:
        model = Irrigation
        fields = "__all__"

class SparepartsForm(forms.ModelForm):
    class Meta:
        model = Spareparts
        fields = "__all__"

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"

class StationeryForm(forms.ModelForm):
    class Meta:
        model = Stationery
        fields = "__all__"

class ConsumablesForm(forms.ModelForm):
    class Meta:
        model = Consumables
        fields = "__all__"

class FungicideForm(forms.ModelForm):
    class Meta:
        model = Fungicide
        fields = "__all__"

class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = "__all__"

class SurfacetantForm(forms.ModelForm):
    class Meta:
        model = Surfacetant
        fields = "__all__"

class HerbicideForm(forms.ModelForm):
    class Meta:
        model = Herbicide
        fields = "__all__"

class PesticideForm(forms.ModelForm):
    class Meta:
        model = Pesticide
        fields = "__all__"
