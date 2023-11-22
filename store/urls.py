
from django.urls import path

from . import views 

urlpatterns = [
    
    path('',views.store,name='store'),
    path('category/<slug:category_url>',views.store,name="products_by_category"),
    path('category/<slug:category_url>/<slug:product_url>',views.product_detail,name="products_detail"),
    path('search',views.search,name = 'search'),
] 