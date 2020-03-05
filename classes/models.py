from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.title}'

class Class(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    lessons = models.ManyToManyField(Lesson)
    LEVEL_CHOICES = [
        ('1', 'Beginner'),
        ('2', 'Novice'),
        ('3', 'Intermediate'),
        ('4', 'Advanced'),
        ('5', 'Expert')
    ]
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, null=True)

    def __str__(self):
        return f'{self.title}'

