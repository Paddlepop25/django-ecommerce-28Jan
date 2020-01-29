from django.urls import path
from .views import show_products, create_product, edit_product, delete_product, show_categories, create_category
   
urlpatterns = [   
    path('', show_products),
    path('create_product/', create_product),
    path('edit_product/<id>', edit_product, name='edit_product_route'),
    path('delete_product/<id>', delete_product),
    path('categories/', show_categories),
    path('create_category/', create_category),
    ]