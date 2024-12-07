from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#User model
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Contact model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    testimonial = models.TextField()
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Notifications(models.Model):
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject

class UserProfile(models.Model):
    prof = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    meter_number = models.CharField(max_length=20)

    def __str__(self):
        return self.prof.name

