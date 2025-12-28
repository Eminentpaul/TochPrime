from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Product, Product_Image

# Create your views here.


def home(request):
    products = Product.objects.all()
    product_images = [Product_Image.objects.filter(product = product)[0] for product in products]


    context = {
        'products': products, 
        "product_images": product_images,
    }
    return render(request, 'store/index.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    colors = product.colour.split(',')
    product_colors = [color.strip() for color in colors]

    sizes = product.size.split(',')
    product_sizes = [size.strip() for size in sizes]

    discount_price = product.price - (product.percent_off/100 * product.price)
    discount_price = round(discount_price, 2)


    context = {
        'product': product,
        'product_colors': product_colors, 
        'product_sizes': product_sizes, 
        'product_images': product.product_image.all(),
        'product_main_images': product.product_image.all()[0],
        'discount_price': discount_price,
    }
    return render(request, 'store/shop-single.html', context)