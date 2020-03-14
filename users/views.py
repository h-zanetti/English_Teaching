from django.shortcuts import render, redirect
from django.contrib import auth, messages
import datetime as dt
from .models import User, Student, Teacher


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

        if request.POST['user_type'] == 'student':
            student = Student.objects.create(user=user)
            student.save()
            print("Student created successfully!")
        elif request.POST['user_type'] == 'teacher':
            teacher = Teacher.objects.create(user=user)
            teacher.save()
            print("Teacher created successfully!")
        else:
            print("You have to choose a user type (Student or Teacher)")
            return redirect('register')

        user.payment_due = dt.date.today() + dt.timedelta(days=7)
        user.save()
        auth.login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwd = request.POST['passwd']
        if User.objects.filter(email=email).exists():
            user = User.objects.filter(email=email).first().check_password(passwd)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    today = dt.date.today()
                    next_payment = user.payment_due - today
                    if next_payment.days <= 7:
                        messages.warning(request, f'Welcome back, {user.first_name}! Your next payment is in {next_payment.days} days')
                    else:
                        messages.success(request, f'Welcome back, {user.first_name}! Your account is up to date.')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Oops.. It looks like your account was deactivated')
                    return redirect('index') # TODO: Send user to payment view
            else:
                messages.error(request, "Email and password doesn't match")
                return redirect('login')
        else:
            messages.error(request, "This email is not registered")
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You signed out successfully, see you soon!')
    return redirect('index')

def dashboard(request):
    context = {
        'user': request.user,
    }
    return render(request, 'users/dashboard.html', context)