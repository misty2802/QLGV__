# Generated by Django 4.0 on 2024-05-23 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_instructor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='user',
        ),
    ]