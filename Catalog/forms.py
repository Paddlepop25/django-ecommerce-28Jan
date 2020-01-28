from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    # inner class
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock')