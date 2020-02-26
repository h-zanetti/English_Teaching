from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.login, name='register'),
    path('logout', views.login, name='logout'),
]