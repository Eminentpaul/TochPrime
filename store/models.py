from django.db import models
import uuid
from user_auth.utils import imageResize
from category.models import Cateory
from uuid import uuid4

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Cateory, on_delete=models.CASCADE,related_name="cate_name")
    colour = models.CharField(max_length=500)
    size = models.CharField(max_length=20)
    reference = models.UUIDField(default=uuid4(), editable=False, unique=True)



class Product_Image(models.Model):
    image = models.ImageField(upload_to='Product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')


    def save(self, *args, **kwargs):
        if self.image:
            self.image = imageResize(self.image)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


    @property
    def product_image(self):
        if self.image:
            return self.image.url

        
