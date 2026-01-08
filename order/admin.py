from django.contrib import admin
from .models import Billing_Address, Shipping_Address, Order

# Register your models here.

class BillingAdmin(admin.ModelAdmin):
    list_display = ['user', 'state', 'country', 'postal_code', 'city', 'address1', 'address2']
    list_display_links = ['user', 'state', 'country', 'postal_code', 'city', 'address1', 'address2']

class ShippingAdmin(admin.ModelAdmin):
    list_display = ['user', 'state', 'country', 'postal_code', 'city', 'address1', 'address2']
    list_display_links = ['user', 'state', 'country', 'postal_code', 'city', 'address1', 'address2']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'amount', 'order_status', 'payment_status', 'updated_at']
    list_display_links = ['order_id', 'user', 'amount', 'order_status', 'payment_status', 'updated_at']
    list_filter = ['order_status', 'payment_status']
    search_fields = ['order_id']



admin.site.register(Billing_Address, BillingAdmin)
admin.site.register(Shipping_Address, ShippingAdmin)
admin.site.register(Order, OrderAdmin)