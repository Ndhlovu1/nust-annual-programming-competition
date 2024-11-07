# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    preferred_programming_language = models.CharField(max_length=50,help_text="e.g. Python", blank=True, null=True)
    past_participation = models.CharField(max_length=50, choices=[('Yes','Yes'),('No','No')], default="Unknown")
    cellphone_number = models.CharField(max_length=50, blank=True, null=True)
    mentor_name = models.CharField(max_length=50, blank=True, null=True)
    mentor_email = models.EmailField(max_length=254, blank=True, null=True)
    mentor_cellphone = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20,choices=[('university', 'University'),('highschool', 'High School'),('sponsor', 'Sponsor'),('volunteer','volunteer'),], default='university')

    def __str__(self):
        return f"{self.user.username}'s Profile"
