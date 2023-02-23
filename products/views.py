from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.
from django.http import HttpResponse

MY_ITEMS = [
    {'id': 1, 'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'id': 2,'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'id': 3,'name': 'wine', 'price': 10.0, 'quantity': 5},
]
from .models import Product,Order
from customers.models import Customer
def productslistView(request):

    products = Product.objects.all()
    context = {
        'object_list':products,
    }
    template_name = "productslist.html"
    return render(request, template_name, context)


def productView(request, id):
    product = Product.objects.get(id=id)
    template_name = "product.html"
    context = {
        'object':product
    }
    return render(request, template_name, context)

