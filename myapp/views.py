from django.shortcuts import render
from .models import Product

def index(request):
    message = "Welcome to my app"
    return render(request, 'index.html', {'message': message})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def about(request):
    return render(request, 'about.html')
