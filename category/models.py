from django.db import models
from user_auth.models import User

# Create your models here.
class Cateory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300, unique=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ['name']
        verbose_name= 'category'
        verbose_name_plural = "Categories"



# class Review(models.Model):
#     from store.models import Product
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
