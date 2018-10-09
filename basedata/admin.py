from django.contrib import admin
from .models import Customer,Product
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):

    fieldsets = [
        ('基本信息',               {'fields': ['CUSTOMERID','Customer_Type','Descr_C']}),
        ('扩展信息', {'fields': ['Address1','Descr_E'] }),
    ]

    list_display = ('CUSTOMERID', 'Customer_Type', 'Descr_C','Address1')
    #list_filter = ['Descr_C']
    search_fields = ['Descr_C']

admin.site.register(Customer, CustomerAdmin)

admin.site.register(Product)