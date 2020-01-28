from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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
    
# edit_product/<id>    
def edit_product(request, id):
    #pk stands for primary key
    product_to_be_edited = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        # print(request.POST)
        form = ProductForm(request.POST, instance=product_to_be_edited)
        if form.is_valid():
            form.save()
            return redirect(show_products)
        else:
            # print (form.errors)
            return HttpResponse("Errors")

    else:
        edit_form = ProductForm(instance=product_to_be_edited)
        return render(request, 'Catalog/edit_product.template.html', {
            'form':edit_form
        })  
        
def delete_product(request, id):
    product_being_deleted = get_object_or_404(Product, pk=id)
    product_being_deleted.delete()
    return redirect(show_products)
        