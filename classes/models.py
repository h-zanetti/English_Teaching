from django.db import models
from users.models import Teacher, Student

class Class(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    lessons = models.ManyToManyField(Lesson)
    LEVEL_CHOICES = [
        ('1', 'Beginner'),
        ('2', 'Novice'),
        ('3', 'Intermediate'),
        ('4', 'Advanced'),
        ('5', 'Expert')
    ]
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)

    def __str__(self):
        return f'{self.title}'

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
