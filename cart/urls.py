from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<str:slug>/', views.add_to_cart, name="add_to_cart"),
    path('remove/<str:pk>/item/', views.remove_item, name="remove_item"),
    path('quantity/<str:pk>/', views.quantity, name="quantity")
]
