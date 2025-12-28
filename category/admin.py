from django.contrib import admin
from .models import Cateory

# Register your models here.
class CateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Cateory, CateAdmin)