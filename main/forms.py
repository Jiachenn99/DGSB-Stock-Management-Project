from django import forms
from main.models import Supplier
from main.models import Purchasing,Category,Tools


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


class OrderForm(forms.Form):
    class Meta: 
        model = Category
        fields = "__all__"
    Category = forms.ModelChoiceField(queryset=Category.objects.values_list('category_name',flat = True).distinct());
    Supplier = forms.ModelChoiceField(queryset=Supplier.objects.order_by('supplier_name').values_list('supplier_name', flat=True).distinct());
    Item_Name = forms.ModelChoiceField(queryset=Tools.objects.order_by('tool_name').values_list('tool_name', flat=True).distinct());
    # Item_Name_Irrigation = forms.ModelChoiceField(queryset=Irrigation.objects.order_by('irrigation_item_name').values_list('irrigation_item_name', flat=True).distinct());
    Quantity = forms.IntegerField(min_value=1)
    Description = forms.CharField()

