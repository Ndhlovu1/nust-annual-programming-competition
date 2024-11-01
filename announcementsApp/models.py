from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='announcement_comments')
    title = models.CharField(max_length=50, default="")
    info = models.TextField(max_length=250, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_announcements', blank=True)

    # Optional: Field to track users emailed
    emailed_users = models.ManyToManyField(User, related_name='emailed_announcements', blank=True)


    def __str__(self):
        return self.title[:20]  # Display the first 20 characters

class Comment(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:20]  # Display the first 20 characters
