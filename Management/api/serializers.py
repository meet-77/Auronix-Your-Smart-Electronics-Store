from Management.models import Category , Product , Order
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id' , 'category_name','category_description']
        
        
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__' 