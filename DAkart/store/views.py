from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from carts.models import CartItem
from django.db import connection
from carts.views import _cart_id 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from category.models import Category 
from . models import Product

# Create your views here.
def store(request,category_url=None):
    categories = None
    products = None
    
    if category_url!= None:
        categories = get_object_or_404(Category,url = category_url)
        products =   Product.objects.all().filter(category = categories,is_available=True)
        paginator = Paginator(products,3)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products,3)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
            'products':paged_products,
            'product_count':product_count
        }
    return render(request,'store.html',context)

def product_detail(request, category_url,product_url):
    try :
        single_product = Product.objects.get(category__url=category_url,slug=product_url)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),is_active=True,product=single_product).exists()
    except Exception as e:
        return e
    context={
        'single_product' : single_product,
        'in_cart' : in_cart
    }
    return render(request,'product-detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context={
       'products':products,
       'product_count':product_count
    }
        
    return render(request,'store.html',context)