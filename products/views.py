from django.shortcuts import render, redirect


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
    orderForm=OrderForm()
    if request.POST:
        orderForm=OrderForm(request.POST)
        if orderForm.is_valid():
            data=orderForm.save(commit=False)
            data.product_id=product
            data.save()
            print(orderForm.cleaned_data,data)
    context = {
        'object':product,
        'form':OrderForm
    }
    return render(request, template_name, context)

from .forms import ProductForm,OrderForm

def eddProductView(request):
    template_name = "addProduct.html"
    form = ProductForm()

    if request.POST:
        form = ProductForm(request.POST)
        print('post test--------')

        if form.is_valid():
            form.save()
            return redirect('product-list')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request,template_name,context)

def editProductView(request,id):

    template_name = 'editProduct.html'
    product = Product.objects.get(id=id)

    form = ProductForm(instance=product)
    if request.POST:
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')

    context = {
    'form':form,
        'product_id':product.id
    }
    return render(request,template_name,context)

def deleteProductView(request,id):
    print('delete datrigerda')
    product = Product.objects.get(id=id)
    if request.POST:
        product.delete()
    return redirect('product-list')

