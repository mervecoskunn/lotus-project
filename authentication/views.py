from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = email.split('@')[0]
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # Check if user exists
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password is incorrect.')

    return render(request, 'authentication/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email.split('@')[0]

        # Check if username or email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'authentication/register.html')
        else:
            new_user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                # Hash the password before saving
                password=make_password(password)
            )
            messages.success(request, 'Account was created for ' +
                             email + '. You can login now.')
        return redirect('login')

    return render(request, 'authentication/register.html',)


def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return render(request, 'authentication/login.html')
