# Generated by Django 3.2 on 2021-09-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], default='student', max_length=10),
        ),
    ]
