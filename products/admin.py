from django.contrib import admin

# Register your models here.
from .models import Product,Order
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','product_id','customer_id')

