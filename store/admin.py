from django.contrib import admin
from .models import Product, Product_Image

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount','size', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['name', 'amount', 'size', 'category']
    search_fields = ['name']
    # list_filter = 


admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Image)