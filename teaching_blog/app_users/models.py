from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

def path_and_rename1(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = 'User_ID_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=500)
    institution = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    id_pic = models.ImageField(upload_to=path_and_rename1, verbose_name="ID Picture", blank=True)
    teacher = 'teacher'
    student = 'student'
    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=student)
    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
