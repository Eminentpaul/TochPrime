from django.db import models
from user_auth.models import User
from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.cart_id
    
    class Meta:
        ordering = ['-created']
    


class Cart_Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.product.name
    
    def get_amount(self):
        if self.product.percent_off:
            return round((self.product.amount - (self.product.amount * self.product.percent_off/100)) * self.quantity, 2)
        else:
            return round(self.quantity * self.product.amount, 2)
        
    @property
    def get_image(self):
        images = self.product.product_image.all()
        
        if images:
            return images.first().image.url