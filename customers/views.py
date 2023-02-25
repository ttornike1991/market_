from django.shortcuts import render,redirect
from .models import   CustomerModel
from . import forms
# Create your views here.

NAME = [{'first_name': "Lali", 'last_name': "Bibilashvili"},{'first_name': "Lali", 'last_name': "Bibilashvili"},]

def customersView(request):
    customers=CustomerModel.objects.all()
    template_name = "customers.html"
    context = {'customers':customers}
    return render(request, template_name, context)
def CustomerView(request, id):
    Customer = CustomerModel.objects.get(id=id)
    template_name = "customer.html"
    context = {
        'object':Customer
    }
    return render(request, template_name, context)
def addCustomer(request):
    template_name = "addCustomer.html"
    form = forms.CustomerForm()

    if request.POST:
        form = forms.CustomerForm(request.POST)
       

        if form.is_valid():
            form.save()
            return redirect('customers')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request,template_name,context)
def editCustomer(request,id):

    template_name = 'editCustomer.html'
    Customer = CustomerModel.objects.get(id=id)

    form = forms.CustomerForm(instance=Customer)
    if request.POST:
        form = forms.CustomerForm(request.POST,instance=Customer)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {
    'form':form,
        'Customer_id':Customer.id
    }
    return render(request,template_name,context)

def deleteCustomer(request,id):
    
    Customer = CustomerModel.objects.get(id=id)
    if request.POST:
        Customer.delete()
    return redirect('customers')