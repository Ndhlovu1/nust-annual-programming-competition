# main/admin.py

from django.contrib import admin
from .models import Question, Answer, Comment, Vote  # Import all the models

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Admin interface for managing questions.
    """
    list_display = ('title', 'user', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('title', 'content')  # Allow searching by title and content
    list_filter = ('created_at', 'user')  # Filter options for the list view

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
    Admin interface for managing answers.
    """
    list_display = ('question', 'user', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('content',)  # Allow searching by answer content
    list_filter = ('created_at', 'user')  # Filter options for the list view

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for managing comments.
    """
    list_display = ('user', 'question', 'answer', 'created_at')  # Fields to display in the list view
    search_fields = ('content',)  # Allow searching by comment content
    list_filter = ('created_at', 'user')  # Filter options for the list view

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    """
    Admin interface for managing votes on answers.
    """
    list_display = ('user', 'answer', 'vote_type')  # Fields to display in the list view
    list_filter = ('vote_type', 'user')  # Filter options for the list view

