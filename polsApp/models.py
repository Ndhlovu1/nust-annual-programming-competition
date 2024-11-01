# polls/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    
    def is_active(self):
        return timezone.now() < self.due_date

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="polls_vote")
    choice = models.CharField(max_length=200)
    
    class Meta:
        unique_together = ('poll', 'user')  # Ensures a user can only vote once per poll
