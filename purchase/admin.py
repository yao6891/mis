from django.contrib import admin
from .models import ASN_Header,ASN_Detail
from basedata.models import Customer
# Register your models here.

class ASN_DetailInline(admin.TabularInline):
    fields = ('ASNLineNo', 'SKU', 'SKUDescrC', 'ExpectedQty', 'PackID', 'ReceivedTime')
    model = ASN_Detail

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 3

class ASN_HeaderAdmin(admin.ModelAdmin):
    list_display = ('ASNNo', 'ASNType', 'ASNStatus', 'CustomerID','ASNReference1','ASNReference3','UserDefine1','UserDefine2','Supplier_Name','ASNCreationTime')
    fieldsets = [
        ('订单汇总',{'fields':['ASNNo','ASNType','ASNStatus', 'SupplierID','ASNReference1','ASNReference3','UserDefine1','UserDefine2','Supplier_Name','ASNCreationTime']}),

    ]
    inlines = [ASN_DetailInline]
    raw_id_fields = ['SupplierID']
    readonly_fields = ['ASNNo', 'ASNStatus']
    search_fields = ['ASNNo', 'Supplier_Name']

admin.site.register(ASN_Header,ASN_HeaderAdmin)

