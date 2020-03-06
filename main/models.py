from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 80)
    class Meta:
        db_table = "Supplier"

    def __str__(self):
        return self.supplier_name

class Purchasing(models.Model):
    purchasing_id = models.AutoField(primary_key=True)
    pv_no = models.CharField(max_length = 20)
    invoice_no = models.CharField(max_length = 20)
    purchasing_date = models.DateField(auto_now=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    description = models.CharField(max_length = 100)
    class Meta:
        db_table = "Purchasing"

    def __str__(self):
        return self.pv_no

class Irrigation(models.Model):
    irrigation_id = models.AutoField(primary_key = True)
    irrigation_item_name = models.CharField(max_length = 50)
    unit_price = models.DecimalField(max_digits = 10, decimal_places= 2, default = 0.00, validators=[MinValueValidator(0.00)])
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    purchasing = models.ForeignKey(Purchasing, on_delete = models.CASCADE)
    description = models.CharField(max_length = 100)
    class Meta:
        db_table = "irrigation"

    def __str__(self):
        return self.irrigation_item_name

class Tools(models.Model):
    tool_id = models.AutoField(primary_key=True)
    tool_name = models.CharField(max_length = 50)
    unit_price = models.DecimalField(max_digits = 10, decimal_places= 2, default = 0.00, validators=[MinValueValidator(0.00)])
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "tools"

    def __str__(self):
        return self.tool_name

class Spareparts(models.Model):
    spare_parts_id = models.AutoField(primary_key = True)
    spare_parts_name = models.CharField(max_length = 30)
    vehicle_assigned = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    spare_parts_unit_price = models.DecimalField(max_digits = 10, decimal_places= 2, default = 0.00, validators=[MinValueValidator(0.00)])
    spare_parts_quantity = models.PositiveIntegerField(default = 0)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "spare_parts"

    def __str__(self):
        return self.spare_parts_name

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True);   
    vehicle_type = models.CharField(max_length = 30)
    vehicle_name = models.CharField(max_length = 50)
    vehicle_number_plate = models.CharField(max_length = 10)
    vehicle_owner = models.CharField(max_length = 30)
    spare_parts_assigned = models.ForeignKey(Spareparts, on_delete=models.CASCADE)
    class Meta:
        db_table = "vehicle"

    def __str__(self):
        return self.vehicle_name

class Stationery(models.Model):
    stationery_id = models.AutoField(primary_key=True)
    stationery_name = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length = 100)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "stationery"

    def __str__(self):
        return self.stationery_name

class Consumables(models.Model):
    consumables_id = models.AutoField(primary_key=True)
    consumables_name = models.CharField(max_length = 50)
    unit_price = models.DecimalField(max_digits = 10, decimal_places= 2, default = 0.00, validators=[MinValueValidator(0.00)])
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length = 100)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "consumables"

    def __str__(self):
        return self.consumables_name

class Fungicide(models.Model):
    fungicide_id = models.AutoField(primary_key=True)
    fungicide_name = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length = 100)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "fungicide"

    def __str__(self):
        return self.fungicide_name

class Fertilizer(models.Model):
    fertilizer_id = models.AutoField(primary_key=True)
    fertilizer_name = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length = 100)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "fertilizer"
    
    def __str__(self):
        return self.fertilizer_name

class Surfacetant(models.Model):
    surfacetant_id = models.AutoField(primary_key=True)
    surfacetant_name = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length = 100)
    Purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "surfacetant"

    def __str__(self):
        return self.surfacetant_name

class Herbicide(models.Model):
    herbicide_id = models.AutoField(primary_key=True)
    herbicide_name = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length = 100)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "herbicide"

    def __str__(self):
        return self.herbicide_name

class Pesticide(models.Model):
    pesticide_id = models.AutoField(primary_key=True)
    pesticide_name = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length = 100)
    purchasing = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "pesticide"

    def __str__(self):
        return self.pesticide_name
        