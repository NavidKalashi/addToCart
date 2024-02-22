from django.shortcuts import render

from .models import Product

# Create your views here.

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/products.html', context)

def cart(request):
    return render(request, 'store/cart.html')