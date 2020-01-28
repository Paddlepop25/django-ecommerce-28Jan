from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=3, blank=False)
    stock = models.IntegerField(blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " x " + str(self.stock) 
        
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name 

        