from django.urls import path
from . import views

from . import views

urlpatterns = [    
    path('', views.customersView, name='customers'),
    path('customer_view/<int:id>/', views.CustomerView, name='customer'),
    path('edit-customer/<int:id>/', views.editCustomer, name='editCustomer'),
    path('add_customer', views.addCustomer, name='addCustomer'),
    path('delete-customer/<int:id>', views.deleteCustomer, name='delCustomer'),
    ]
