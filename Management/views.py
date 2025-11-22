from django.shortcuts import render , get_object_or_404 , redirect
from Management.models import Category , Product , Order , User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout   
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, UpdateView


User = get_user_model()

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address
        )
        user.set_password(password)
        user.save()

        login(request, user)
        return redirect("login")

    return render(request, "register.html")
    
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password")
            return render(request, "login.html")

        login(request, user)
        return redirect("dashboard")

    return render(request, "login.html")

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect("management:login")


class UserListView(ListView):
    model = User
    template_name = "user_list.html"  
    context_object_name = "users"
    paginate_by = 20

class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"
    context_object_name = "user_obj"

class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone', 'address']
    template_name = "user_form.html"
    success_url = reverse_lazy('user-list')

    def get_object(self, queryset=None):
        # Using pk from URL
        return get_object_or_404(User, pk=self.kwargs.get('pk'))
    
def dashboard(request):
    category = Category.objects.all()
    product = Product.objects.all()
    users = User.objects.all()  

    total_product = Product.objects.count()
    total_category = Category.objects.count()
    total_user = User.objects.count()
    total_order = Order.objects.count()

    context = {
        'product': product,
        'category': category,
        'users': users,   
        'products': product,  
        'total_product': total_product,
        'total_category': total_category,
        'total_user': total_user,
        'total_order':total_order,
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

 
def ordermanage(request):
    order = Order.objects.select_related('product', 'product__category').all()
    return render(request, 'manageorder.html', {'order': order})

 
def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    users = User.objects.all()
    products = Product.objects.all()

    if request.method == "POST":
        customer_id = request.POST.get('customer')
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity'))   # FIXED

        order.customer = User.objects.get(id=customer_id)
        order.product = Product.objects.get(id=product_id)
        order.quantity = quantity
        order.save()  # save() recalculates total

        return redirect('manageorder')

    return render(request, 'order_update.html', {
        'order': order,
        'users': users,
        'products': products
    })
 
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    messages.success(request, "Order deleted successfully!")
    return redirect('manageorder')

 
def manage_user(request):
    users = User.objects.all()  
    return render(request, 'Manageuser.html', {'users': users})

 
