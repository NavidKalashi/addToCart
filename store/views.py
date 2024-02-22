from django.shortcuts import render

from .models import Product, Order

# Create your views here.

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/products.html', context)

def cart(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'store/cart.html', context)