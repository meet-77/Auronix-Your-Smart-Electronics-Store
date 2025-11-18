from decimal import Decimal
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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.IntegerField()
    available = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='category')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_amount(self):
        if self.product and self.quantity:
            return self.product.price * Decimal(int(self.quantity))
        return Decimal('0.00')

    def save(self, *args, **kwargs):
        # ensure quantity is integer
        self.quantity = int(self.quantity or 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer} - {self.product}"
