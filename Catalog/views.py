from django.shortcuts import render
from .models import Product

# Create your views here.
def hello(request):
    return render(request, 'Catalog/index.template.html')

def show_products(request):
    all_products = Product.objects.all() 
    return render(request, 'Catalog/products.template.html', {
        'catalog': all_products
    })