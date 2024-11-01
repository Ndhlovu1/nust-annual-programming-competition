# main/models.py

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Question(models.Model):
    """
    Represents a question posted by a user in the forum.
    """
    title = models.CharField(max_length=255)  # The title of the question
    content = models.TextField()  # The main content/body of the question
    image = models.ImageField(upload_to='questions/', null=True, blank=True)  # Optional image upload field for the question
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who posted the question
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the question was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the question was last updated
    tags = TaggableManager()  # TaggableManager from django-taggit for tagging questions

    def __str__(self):
        return self.title  # Return the title of the question for easy identification


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    image = models.ImageField(upload_to='answers/', null=True, blank=True)  # Image upload field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.PositiveIntegerField(default=0)  # Field to track upvotes
    downvotes = models.PositiveIntegerField(default=0)  # Field to track downvotes

    def __str__(self):
        return self.content[:50] 

class Comment(models.Model):
    """
    Represents a comment on a specific answer or question in the forum.
    """
    content = models.TextField()  # The content/body of the comment
    image = models.ImageField(upload_to='comments/', null=True, blank=True)  # Optional image upload field for the comment
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='forum_comments')  # The user who posted the comment
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')  # Related question, if applicable
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')  # Related answer, if applicable
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the comment was created

    def __str__(self):
        return f'Comment by {self.user} on {self.answer or self.question}'  # Return a string representation of the comment

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who voted
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)  # Answer being voted on
    vote_type = models.BooleanField()  # True for upvote, False for downvote

    class Meta:
        unique_together = ('user', 'answer')  # Ensure a user can only vote once per answer

    def __str__(self):
        return f"{self.user.username} {'upvoted' if self.vote_type else 'downvoted'} answer {self.answer.id}"
