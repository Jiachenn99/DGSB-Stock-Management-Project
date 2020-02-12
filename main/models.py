from django.db import models

# Create your models here.
class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 80)
    class Meta:
        db_table = "supplier"


class Purchasing(models.Model):
    purchasing_id = models.AutoField(primary_key=True)
    pv_no = models.CharField(max_length = 20)
    invoice_no = models.CharField(max_length = 20)
    purchasing_date = models.CharField(max_length = 20)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    description = models.CharField(max_length = 100)
    class Meta:
        db_table = "purchasing"