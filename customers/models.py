from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=30,default='retailer')

    def __str__(self):
        return f'{self.first_name[0].capitalize()}.{self.last_name.capitalize()}'
class CustomerModel(models.Model):
    f_name= models.CharField(max_length=50, blank=False, null=False, default='',
                              help_text='Enter your first name')
    l_name= models.CharField(max_length=50, blank=False, null=False, default='',
                              help_text='Enter your first name')
    birth_date= models.DateField(blank=False, null=False, default=timezone.now,
                                   help_text='Enter your birth date')
    is_valide=models.BooleanField(default=False)
    email=models.EmailField(max_length=254, unique=True, blank=False, null=False,
                              help_text='Enter your email address')
    class Meta:
         
        verbose_name_plural = 'Customers'
    def __str__(self):
        return self.f_name + ' ' + self.l_name

    def verbose_name(self):
        return 'CustomerModel'