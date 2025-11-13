from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField( max_length=50)
    category_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    price = models.IntegerField()
    product_stock =  models.IntegerField()
    available = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    created_at = models.DateTimeField(auto_now_add=True)
    
        
    def __str__(self):
        return self.product_name
    