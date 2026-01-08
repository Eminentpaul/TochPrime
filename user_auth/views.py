from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User

# # Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
    return render(request, 'user_auth/login.html')