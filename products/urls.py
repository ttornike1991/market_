from django.urls import path
from .views import productslistView, productView,eddProductView,editProductView,deleteProductView
from . import views

urlpatterns = [
    path('product-list',productslistView, name="product-list"),
    path('add-product',eddProductView,name="add-product"),
    path('edit-product/<int:id>',editProductView,name='edit-product'),
    path('delete-product/<int:id>',deleteProductView,name='delete-product'),
    path('product/<int:id>/',productView, name="product"),

]
