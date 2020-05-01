from django import forms
from main.models import *
from django.forms import ModelChoiceField

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

class OrderForm(forms.Form):
    email = forms.ModelChoiceField(queryset=Supplier.objects.values_list('email',flat = True).distinct(),to_field_name='email')
    # def __init__(self, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].queryset = Supplier.objects.all()
    #     self.fields['email'].label_from_instance = lambda obj: "%s" % (obj.supplier_name)
    
    subject = ''
    message = forms.CharField(widget=forms.Textarea, required=True)
    
