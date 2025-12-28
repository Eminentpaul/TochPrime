from django.db import models
from user_auth.utils import imageResize
from category.models import Cateory
from uuid import uuid4
from django.utils.safestring import mark_safe

# Create your models here.


RATE_LEVEL = (
    ('1', '1 Star'),
    ('2', '2 Stars'),
    ('3', '3 Stars'),
    ('4', '4 Stars'),
    ("5", '5 Stars'),
)




class Product(models.Model):
    # vendor = models.ForeignKey()
    name = models.CharField(max_length=250)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=12, max_length=12)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Cateory, on_delete=models.CASCADE,related_name="cate_name")
    colour = models.CharField(max_length=500)
    size = models.CharField(max_length=200, default="38, 39, 40, 41, 42, 43, 44, 45")
    reference = models.UUIDField(default=uuid4(), editable=False, unique=True)
    star_rating = models.CharField(max_length=20, choices=RATE_LEVEL, null=True, blank=True)
    percent_off = models.DecimalField(max_length=6, decimal_places=2, max_digits=6, default=0.00)

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.name 
    
    class Meta:
        ordering = ['-created']
    

    # def image_tag(self):
    #     if self.image:
    #         return mark_safe('<img src="%s" style="width: 45px; height:auto;" />' % self.image.url)
    #     else:
    #         return 'No Image Found' 
    # image_tag.short_description = 'Image'



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

        

class Cart(models.Model):
    