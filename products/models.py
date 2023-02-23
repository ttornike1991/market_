from django.db import models
from customers.models import Customer
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()

    def save(self):
        #customization
        if self.quantity > 100:
            super(Product,self).save()


    def __str__(self):
        return self.name

class Order(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


