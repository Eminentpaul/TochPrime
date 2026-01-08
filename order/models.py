from django.db import models
from user_auth.models import User
from cart.models import Cart_Item, Cart
import uuid

# Create your models here.
class Billing_Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=30)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.user.fullname



class Shipping_Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=30)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.user.get_full_name




class Order(models.Model):
    cart = models.ForeignKey(Cart_Item, on_delete=models.CASCADE, related_name='order_cart')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=255)
        
    # Use a UUID for the reference ID for security
    payment_reference = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    PAYMENT_STATUS = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
    )

    ORDER_STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='PENDING')
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS, default='New')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.fullname} - {self.payment_status}"
    

    class Meta:
        ordering = ['-updated_at']