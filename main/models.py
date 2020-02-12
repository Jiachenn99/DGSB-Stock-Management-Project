from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Supplier(models.Model):
    Supplier_ID = models.AutoField(primary_key=True)
    Supplier_Name = models.CharField(max_length = 50)
    Description = models.CharField(max_length = 80)
    class Meta:
        db_table = "supplier"


class Purchasing(models.Model):
    Purchasing_ID = models.AutoField(primary_key=True)
    PV_No = models.CharField(max_length = 20)
    Invoice_No = models.CharField(max_length = 20)
    Purchasing_Date = models.CharField(max_length = 20)
    Supplier_ID = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Description = models.CharField(max_length = 100)
    class Meta:
        db_table = "purchasing"

class Irrigation(models.Model):
    Irrigation_ID = models.AutoField(primary_key = True)
    Irrigation_ItemName = models.CharField(max_length = 50)
    Unit_Price = models.DecimalField(max_digits = 10, decimal_places= 2, default = 0.00, validators=[MinValueValidator(0.00)])
    Quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    Purchasing_ID = models.ForeignKey(Purchasing, on_delete = models.CASCADE)
    Description = models.CharField(max_length = 100)
    class Meta:
        db_table = "irrigation"

class Tools(models.Model):
    Tool_ID = models.AutoField(primary_key=True)
    Tool_Name = models.CharField(max_length = 50)
    Unit_Price = models.DecimalField(max_digits = 10, decimal_places= 2, default = 0.00, validators=[MinValueValidator(0.00)])
    Quantity = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0)])
    Purchasing_ID = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    class Meta:
        db_table = "tools"
