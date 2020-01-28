from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=3, blank=False)
    stock = models.IntegerField(blank=False)

    def __str__(self):
        return self.name + " x " + str(self.stock) 
        

        