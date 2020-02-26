from django.db import models
from user.models import Student, Teacher

class Class(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student)
