from django.db import models

# Create your models here.
class Cateory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300, unique=True)

    def __str__(self):
        return self.category_name
    
    class Meta: 
        ordering = ['name']
        verbose_name= 'category'
        verbose_name_plural = "Categories"



class Review(models.Model):
    