from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('product/<str:slug>/details/', views.product_detail, name='product_detail'), 
]