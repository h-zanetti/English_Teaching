from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def login(request):
    return render(request, 'user/login.html')

def register(request):
    form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def logout(request):
    pass