from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        full_name = request.POST['full_name']
        birth_dt = request.POST['birth_dt']
        gender = request.POST['gender']
        passwd = request.POST['passwd']
        passwd2 = request.POST['passwd2']
        if not full_name.strip():
            print("The field 'Full Name' is required")
            return redirect('register')
        if not email.strip():
            print("The field 'Email' is required")
            return redirect('register')
        if passwd != passwd2:
            print("Passwords don't match")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            print("User already registered")
            return redirect('login')
        first_name = full_name.split(' ')[0]
        last_name = full_name.split(' ')[-1]
        user = User.objects.create(
            email=email,
            full_name=full_name,
            first_name=first_name,
            last_name=last_name,
            password=passwd,
            birth_dt=birth_dt,
            gender=gender
        )
        user.save()
        print("User registered successfully!")
        return redirect('login')
    else:
        return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwd = request.POST['passwd']
        if User.objects.filter(email=email).exists():
            user = User.objects.filter(email=email).first().check_password(passwd)
            if user is not None:
                auth.login(request, user)
                print("Welcome back!")
                return redirect('dashboard')
            else:
                print("Email and password doesn't match")
                print(f"{email} | {passwd}")
                return redirect('login')
        else:
            print("This email is not registered")
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    return render(request, 'users/dashboard.html')