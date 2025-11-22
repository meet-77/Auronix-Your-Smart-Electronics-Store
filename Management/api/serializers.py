from Management.models import Category , Product , Order , User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id' , 'category_name','category_description']
        
        
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 
        
class OrderSerializer(serializers.ModelSerializer):
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'address', 'password']

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        