from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
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
            username=full_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=passwd
        )
        user.save()
        print("User registered successfully!")
        return redirect('login')
    else:
        return render(request, 'user/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwd = request.POST['passwd']
        
        return redirect('dashboard')
    else:
        return render(request, 'user/login.html')

def logout(request):
    pass

def dashboard(request):
    return render(request, 'user/dashboard.html')