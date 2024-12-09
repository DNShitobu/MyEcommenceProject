from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Product

def index(request):
    return render(request, 'store/index.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def product_list(request):
    products = Product.objects.all()  # Retrieve all products
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Retrieve specific product
    return render(request, 'store/product_detail.html', {'product': product})

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin)
def admin_dashboard(request):
    # Only Admins can access this view
    return render(request, 'store/admin_dashboard.html')

def seller_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.groups.filter(name='Seller').exists() and product.seller == request.user:
        return render(request, 'store/seller_product_edit.html', {'product': product})
    else:
        # Redirect to an error page or show a message
        return redirect('error_page')