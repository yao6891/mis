from django.db import models

# Create your models here.
class Customer(models.Model):
    SEX = (
        ('CO', '收货人'),
        ('OW', '货主'),
    )
    CUSTOMERID = models.CharField(max_length=30,unique=True,primary_key=True)
    Customer_Type = models.CharField(max_length=2, choices=SEX)
    Descr_C = models.CharField(max_length=200)
    Descr_E = models.CharField(max_length=200)
    Address1 = models.CharField(max_length=200)


    def __str__(self):
        return self.Descr_C

    class Meta:
        db_table = 'bas_CUSTOMER'

class Product(models.Model):
    CustomerID = models.CharField(max_length=30)
    SKU = models.CharField(max_length=50,primary_key=True)
    Descr_C = models.CharField(max_length=200)
    Descr_E = models.CharField(max_length=200)
    Alternate_SKU1 = models.CharField(max_length=100)
    Alternate_SKU2 = models.CharField(max_length=100)
    Alternate_SKU4 = models.CharField(max_length=100)
    Alternate_SKU5 = models.CharField(max_length=100)
    SKU_Group2 = models.CharField(max_length=100)

    def __str__(self):
        return self.Descr_C

    class Meta:
        db_table = 'bas_sku'