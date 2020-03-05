from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def classes(request):
    return render(request, 'classes/main.html')