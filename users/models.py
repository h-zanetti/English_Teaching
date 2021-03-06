from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
import datetime as dt
from classes.models import Class

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=100)
    birth_dt = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    payment_due = models.DateField(null=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birth_dt', 'gender']
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    def check_password(self, raw_password):
        if self.password == raw_password:
            return self
        else:
            return None
    
    def is_student(self):
        return Student.objects.filter(user_id=self.id).exists()

    def is_teacher(self):
        return Teacher.objects.filter(user_id=self.id).exists()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return f'{self.user.full_name}'

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return f'{self.user.full_name}'