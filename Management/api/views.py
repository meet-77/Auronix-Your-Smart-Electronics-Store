from django.shortcuts import render, redirect , get_object_or_404 
from Management.models import Category, Product , Order
from Management.api.serializers import CategorySerializers , ProductSerializers , OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def add_category(request):
    
    if request.method == 'POST':
        name = request.POST.get('category_name')
        description = request.POST.get('category_description')

        if name and description:
            Category.objects.create(
                category_name=name,
                category_description=description
            )
            return redirect('dashboard')

    categorys = Category.objects.all()
    return render(request, 'dashboard.html', {'categorys': categorys})

class CategoryAPIView(APIView):
    def get(self, request):
        categorys = Category.objects.all()
        serializer = CategorySerializers(categorys, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategorydetalisAPIView(APIView):
    
    def get(self , pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializers(category )
        return Response(serializer.data)
    
    def put(self, request , pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
                
    def delete(self ,request , pk):
        category = get_object_or_404(Category,pk=pk)
        category.delete()
        return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)            
        
def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_price = request.POST.get('price')
        product_stock = request.POST.get('product_stock')
        product_check = request.POST.get('available')
        category_id = request.POST.get('category')
 
        available = True if product_check == 'on' else False
 
        if product_name and product_description and product_price and product_stock and category_id:
            Product.objects.create(
                product_name=product_name,
                product_description=product_description,
                price=product_price,
                product_stock=product_stock,
                available=available,   
                category_id=category_id,
            )
            return redirect('dashboard')
 
    category = Category.objects.all()
    product = Product.objects.all()
    return render(request, 'dashboard.html', {'product': product, 'category': category})

          
class ProductAPIView(APIView):
    
    def get(self , requets):
        products = Product.objects.all()
        serializer = ProductSerializers(products,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductdetailsAPIView(APIView):
    
    def get(self , pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    
    def put(self , pk , request):
        product = get_object_or_404(Product , pk=pk)
        serializer = ProductSerializers(product , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , pk):
        product =get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)           
    

class OrderAPIView(APIView):
    
    def get(self,request):    
        order = Order.objects.all()
        serializer = OrderSerializer(order , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)    
    
    
class OrderdetailsAPIView(APIView):
    
    def get(self , pk):
        
        order = get_object_or_404(Order,pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def put(self , pk , request):
        order = get_object_or_404(Order ,  pk=pk)
        serializer = OrderSerializer(order , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self , request , pk):
        order = get_object_or_404(Order ,pk=pk)
        order.delete()
        return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)           
    