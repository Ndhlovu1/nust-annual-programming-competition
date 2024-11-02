# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_STATUS_CHOICES = [
        ('university', 'University'),
        ('highschool', 'High School'),
        ('sponsor', 'Sponsor'),
        ('staff', 'Staff'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=USER_STATUS_CHOICES, blank=True)

    def __str__(self):
        return self.user.username
