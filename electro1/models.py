
from django.db import models


# Create your models here.
#User model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
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

#Team member model
class TeamMember(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#testimonials model
class Testimonials(models.Model):
    testimonial = models.TextField()
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#notificatoins model
class Notifications(models.Model):
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject

# UserProfile now links to Customer model with a OneToOneField
class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    meter_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.phone_number

class Payment(models.Model):
    meter_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.meter_number

class ProfileSettings(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class NotificationSettings(models.Model):
    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)

    def __str__(self):
        return f"Email: {self.email_notifications}, SMS: {self.sms_notifications}"


class SecuritySettings(models.Model):
    two_factor_auth = models.BooleanField(default=False)
    change_password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"2FA: {self.two_factor_auth}"
