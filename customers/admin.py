from django.contrib import admin
from .models import Customer,CustomerModel
# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('id','first_name','last_name')
# @admin.register(CustomerModel)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display = ('id',' f_name','l_name','birth_date','is_valide','email')
admin.site.register(CustomerModel)