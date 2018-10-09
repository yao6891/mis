from django.db import models
from basedata.models import Customer
# Create your models here.
class ASN_Header(models.Model):
    ASNNo = models.CharField(max_length=20,unique=True,primary_key=True)
    ASNType = models.CharField(max_length=20)
    ASNStatus = models.CharField(max_length=2)
    CustomerID = models.CharField(max_length=30)
    ASNReference1 = models.CharField(max_length=50)
    ASNReference3 = models.CharField(max_length=50)
    UserDefine1 = models.CharField(max_length=200)
    UserDefine2 = models.CharField(max_length=200)
    SupplierID = models.ForeignKey(Customer,on_delete=models.CASCADE,to_field="CUSTOMERID",db_column='SupplierID')
    Supplier_Name = models.CharField(max_length=200)
    ASNCreationTime = models.DateTimeField()

    def __str__(self):
        return self.ASNNo

    class Meta:
        db_table = 'DOC_ASN_Header'


class ASN_Detail(models.Model):
    ASNNo = models.ForeignKey(ASN_Header,on_delete=models.CASCADE,to_field="ASNNo",db_column='ASNNo')
    ASNLineNo = models.IntegerField()
    SKU = models.CharField(max_length=50)
    SKUDescrC = models.CharField(max_length=200)
    SKUDescrE = models.CharField(max_length=200)
    ReceivedTime = models.DateTimeField()
    ExpectedQty = models.DecimalField(max_digits=18,decimal_places=8,blank=True,null=True,default=0.00)
    PackID = models.CharField(max_length=40)

    class Meta:
        db_table = 'DOC_ASN_DETAILS'



