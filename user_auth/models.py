from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, unique=True)