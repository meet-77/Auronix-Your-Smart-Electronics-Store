from django.shortcuts import render
from Management.models import Category , Product
# Create your views here.

def dashboard(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'product':product,
        'category':category,
    }
    return render(request, 'dashboard.html', context)