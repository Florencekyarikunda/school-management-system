# Generated by Django 3.2.5 on 2021-09-07 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_remove_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='.jpeg', upload_to='images'),
        ),
    ]
