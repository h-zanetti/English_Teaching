from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Class


def index(request):
    return render(request, 'index.html')

@login_required
def classes(request):
    context = {
        'classes': Class.objects.all(),
    }
    return render(request, 'classes/classes_dashboard.html', context)

@login_required
def clss(request, class_id):
    context = {
        'clss': Class.objects.get(id=class_id),
    }
    return render(request, 'classes/class.html', context)