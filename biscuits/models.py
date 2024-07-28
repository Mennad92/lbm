from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70)
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    illustration = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Delivery(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def deliver_order(self, order):
        self.status = "delivered"
        self.save


    def change_status(self, new_status):
        self.status = new_status
        self.save()

    def __str__(self):
        return f"Transaction {self.id} - Status: {self.status}"
    
    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"

