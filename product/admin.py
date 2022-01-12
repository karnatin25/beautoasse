from django.contrib import admin
from .models import Product_Beato
# Register your models here.

class Product_data(admin.ModelAdmin):
    list_display=['name','description','cost_per_item','stock_quantity','volume']
admin.site.register(Product_Beato,Product_data)
