from django.contrib import admin
from Management.models import Category , Product , Order
# Register your models here. 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','category_description']
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_description','product_stock','price','available','category']
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'customer','quantity' , 'total_amount']
    
    
    


