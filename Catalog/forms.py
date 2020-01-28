from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):

    # inner class
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock', 'category')
        
class CategoryForm(forms.ModelForm):

    # inner class
    class Meta:
        model = Category
        fields = ('name', )        