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


# class OrderForm(forms.Form):
#     class Meta: 
#         model = Category
#         fields = "__all__"
#     Category = forms.ModelChoiceField(queryset=Category.objects.values_list('category_name',flat = True).distinct());
#     Supplier = forms.ModelChoiceField(queryset=Supplier.objects.order_by('supplier_name').values_list('supplier_name', flat=True).distinct());
#     # Item_Name = forms.ModelChoiceField(queryset=Tools.objects.order_by('tool_name').values_list('tool_name', flat=True).distinct());
#     # Item_Name_Irrigation = forms.ModelChoiceField(queryset=Irrigation.objects.order_by('irrigation_item_name').values_list('irrigation_item_name', flat=True).distinct());
#     Quantity = forms.IntegerField(min_value=1)
#     Description = forms.CharField()


# class EmailModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return "%s" % (obj.email)

class OrderForm(forms.Form):
    #email = forms.EmailField(required=True)

    #email = EmailModelChoiceField(queryset=Supplier.objects.all())
    email = forms.ModelChoiceField(queryset=Supplier.objects.values_list('email',flat = True).distinct(),to_field_name='email')
    # def __init__(self, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].queryset = Supplier.objects.all()
    #     self.fields['email'].label_from_instance = lambda obj: "%s" % (obj.supplier_name)
    
    subject = ''
    message = forms.CharField(widget=forms.Textarea, required=True)
    
