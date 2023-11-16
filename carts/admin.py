from django.contrib import admin

from carts.models import Cart
from .models import CartItem

# Register your models here.
admin.site.register(Cart),
admin.site.register(CartItem)
