from django.db import models

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