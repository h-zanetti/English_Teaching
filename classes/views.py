from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Class
from users.models import Student


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

@login_required
def enroll(request, class_id):
    clss = Class.objects.get(id=class_id)
    user = request.user
    student = Student.objects.get(user_id=user.id)
    student.classes.add(clss)
    return redirect('dashboard')
