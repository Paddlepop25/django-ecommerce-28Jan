from django.shortcuts import render, HttpResponse, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.
def hello(request):
    return render(request, 'Catalog/index.template.html')

def show_products(request):
    all_products = Product.objects.all() 
    return render(request, 'Catalog/products.template.html', {
        'catalog': all_products
    })
    
        
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST) # create a form that is filled with whatever the user has typed in
        # the user has submitted form
        if form.is_valid():
            form.save()
            return redirect(show_products)

    else:
        product_form = ProductForm()

        return render(request, 'Catalog/create_product.template.html', {
            'form':product_form
    })            