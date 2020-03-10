from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classes', views.classes, name='classes'),
    path('classes/<int:class_id>', views.clss, name='clss'),
    path('enroll/<int:class_id>', views.enroll, name='enroll'),
]