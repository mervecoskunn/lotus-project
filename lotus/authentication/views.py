from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.


def login(request):
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
