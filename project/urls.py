from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    # My Aps Urls 
    path('user', include('user_auth.urls')),
    path('', include('store.urls')),
]
