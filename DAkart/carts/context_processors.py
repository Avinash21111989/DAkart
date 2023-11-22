from django.http import HttpResponse
from carts.models import Cart,CartItem
from carts.views import _cart_id

def cartCounter(request):
    cart_count = 0
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.all().filter(cart = cart,is_active=True)
        for cart_item in cart_items:
            cart_count += cart_item.quantity
    except Cart.DoesNotExist:
            cart_count = 0

    return dict(count=cart_count)
     
    