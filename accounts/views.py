from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':

        # Login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home:index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'authentication/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        name = request.POST['full-name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is being used')
            else:
                user = User.objects.create_user(
                    first_name=name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                messages.success(request, 'User was created. Now you can log in')
                return redirect('login')
    return render(request, 'authentication/registration.html')
