from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    about = models.TextField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'your order is {self.product.name}'