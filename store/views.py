# Create views for store. 
from itertools import product
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from store.models import Variation
from category.models import Category 
from store.models import Product
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator

# Create your views here. 
# Create your function here. 
def store(request,category_url=None): 
    categories = None 
    products = None 
    if category_url!=None: 
        categories = get_object_or_404(Category,url = category_url) 
        products = Product.objects.all().filter(category = categories, is_available = True).order_by('created_date') 
        paginator = Paginator(products,3)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
    else: 
     
        products = Product.objects.all().filter(is_available = True).order_by('created_date')  
        paginator = Paginator(products,3)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        
    product_count = products.count() 
    context= { 
        'products' :paged_products, 
        'product_count' : product_count
    } 
 
    return render(request,'store.html',context) 
def product_detail(request,category_url,product_url): 
    try: 
        single_product = Product.objects.get(category__url=category_url,slug=product_url)        
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product = single_product,is_active = True).exists()
        variation_exist = Variation.objects.all().filter(product = single_product).exists()
        
    except Exception as e: 
        raise e  
    context={ 
        'single_product': single_product,
        'in_cart' : in_cart,
        'variation_exist' : variation_exist,
        
        
    } 
    return render(request,'product-detail.html',context) 
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
        context = {
        'products': products,
        'product_count':product_count        
        
        }
        
            
    return render(request,'store.html',context)
