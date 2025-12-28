from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'username', 'email', 'phone']
    list_display_links = ['fullname', 'username', 'email', 'phone']



admin.site.register(User, UserAdmin)