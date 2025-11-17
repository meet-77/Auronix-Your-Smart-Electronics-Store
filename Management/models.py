from django.db import models
from django.contrib.auth.models import User
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
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if self.product:
            self.total_amount = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer} - {self.product}"


    