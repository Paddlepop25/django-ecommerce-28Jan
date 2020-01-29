"""EcommerceProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Catalog.views import hello, show_products, create_product, edit_product, delete_product, show_categories, create_category
# from Accounts.views import index as accounts_index, logout, login, profile, register

# path: route in url, function from views, name pass to views(redirect(reverse)...)
# when the user go to user/register route, it will call the register function and i'll call this route register as well
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('product/', include('Catalog.urls')),
    path('user/', include('Accounts.urls')),
    path('user/', include('django.contrib.auth.urls')),
]
