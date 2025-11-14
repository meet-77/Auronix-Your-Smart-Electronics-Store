from django.shortcuts import render , get_object_or_404 , redirect
from Management.models import Category , Product
from django.contrib import messages
# Create your views here.

def dashboard(request):
    category = Category.objects.all()
    product = Product.objects.all()
    total_product = Product.objects.count()
    total_category = Category.objects.count()
    context = {
        'product':product,
        'category':category,
        'total_product':total_product,
        'total_category':total_category,
    }
    return render(request, 'dashboard.html', context)



def managecategory(request):
    category = Category.objects.all()
    return render(request , 'Managecategory.html',{'category':category})

def edit_category(request , id):
    category = get_object_or_404(Category,id=id)
    
    if request.method == "POST":
        category.category_name = request.POST.get('category_name')
        category.category_description = request.POST.get('category_description')
        category.save()
        messages.success(request, "category updated successfully!")
        return redirect('managecategory')
    
    return render(request , 'edit_category.html', {'category':category})


def delete_category(request , id):
    category = get_object_or_404(Category,id=id)
    category.delete()
    messages.success(request, "category deleted successfully!")
    return redirect('managecategory')


def manageproduct(request):
    product = Product.objects.select_related('category').all()
    return render(request , 'manageproduct.html' , {'product':product})


def edit_product(request , id):
    product = get_object_or_404(Product , id=id)
    categorys = Category.objects.all()
    
    
    if request.method == "POST":
        product.product_name = request.POST.get('product_name')
        product.product_description = request.POST.get('product_description')
        product.product_stock = request.POST.get('product_stock')
        product.price = request.POST.get('price')
        product.available = request.POST.get('available')
        category_id = request.POST.get('category')
        product.category = Category.objects.get(id=category_id) if category_id else None
        product.save()
        return redirect('manageproduct')
    return render(request , 'edit_product.html', {'product':product , 'categorys':categorys})
    
    
def delete_product(request , id):
    product = get_object_or_404(Product,id=id)
    product.delete()
    messages.success(request, "product deleted successfully!")
    return redirect('manageproduct')