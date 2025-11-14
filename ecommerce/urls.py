"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Management.api.views import add_category, add_product
from Management.views import dashboard , managecategory , edit_category , delete_category , manageproduct , edit_product, delete_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_category/', add_category, name='add_category'),
    path('managecategory/', managecategory , name='managecategory'),
    path('edit_category/<int:id>/',edit_category, name='edit_category'),
    path('delete_category/<int:id>/', delete_category , name='delete_category'),
    path('add_product/', add_product, name='add_product'),
    path('manageproduct/', manageproduct, name='manageproduct'),
    path('edit_product/<int:id>/', edit_product, name='edit_product'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('ecommerce/', include('Management.api.urls')),
]

