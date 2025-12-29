from django.shortcuts import render, redirect
from .models import Cart, Cart_Item
from django.shortcuts import get_list_or_404, get_object_or_404
from store.models import Product, Product_Image
from .utils import _cart_id

# Create your views here.
def cart(request):
    total = 0
    if request.user.is_authenticated:
        user = request.user
        cartItems = Cart_Item.objects.filter(user=user, is_active=True)
    else:
       cartItems = Cart_Item.objects.filter(cart__cart_id=_cart_id(request), is_active=True)
    
    for item in cartItems:
        total += int(item.get_amount())


    context = {
        'cartItems': cartItems,
        'total': round(total, 2),
    }

    return render(request, 'cart/shop-cart.html', context)




def add_to_cart(request, slug):
    global user
    if request.user.is_authenticated:
        
        user = request.user

    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        color = request.POST.get('p_color')
        size = request.POST.get('size')
        quantity = request.POST.get('quantity')

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()



    try:
        if request.user.is_authenticated:
            cartItems = Cart_Item.objects.get(user=request.user, 
                                              size=size, color=color, 
                                              product=product, is_active=True)

            cartItems.product = product
            cartItems.color = color
            cartItems.size = size
            cartItems.quantity += int(quantity)

            cartItems.save()

            return redirect('cart')
    
        else:
            cartItems = Cart_Item.objects.get(cart=cart, size=size, 
                                              color=color, product=product, 
                                              is_active=True)
            cartItems.product = product
            cartItems.color = color
            cartItems.size = size
            cartItems.quantity += int(quantity)

            cartItems.save()

            return redirect('cart')

        
    
    except Cart_Item.DoesNotExist:
        if request.user.is_authenticated:
            Cart_Item.objects.create(
                user=request.user,
                product=product,
                color=color,
                size=size,
                quantity=int(quantity)
            ) 
        else:
            Cart_Item.objects.create(
                cart=cart,
                product=product,
                color=color,
                size=size,
                quantity=int(quantity)
            ) 



    return redirect('cart')



def quantity(request, pk):
    item = get_object_or_404(Cart_Item, id=pk)
    determine = request.GET.get('q')

    if determine == "1":
        item.quantity += 1
        item.save()
    else:
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

    return redirect('cart')
    


def remove_item(request, pk):
    cart = get_object_or_404(Cart_Item, id=pk)
    cart.delete()

    return redirect('cart')