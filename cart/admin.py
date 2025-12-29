from django.contrib import admin
from .models import Cart, Cart_Item
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'created']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'size', 'quantity', 'user', 'cart']


admin.site.register(Cart, CartAdmin)
admin.site.register(Cart_Item, CartItemAdmin)