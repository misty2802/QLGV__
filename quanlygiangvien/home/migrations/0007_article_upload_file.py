# Generated by Django 4.0 on 2024-05-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_instructor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
