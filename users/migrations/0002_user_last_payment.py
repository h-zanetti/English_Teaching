# Generated by Django 3.0.3 on 2020-03-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_payment',
            field=models.DateField(null=True),
        ),
    ]
