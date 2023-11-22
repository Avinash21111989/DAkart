from django.shortcuts import render
from store.models import Product

def welcome(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products':products
    }
    return render(request,'welcome.html',context)