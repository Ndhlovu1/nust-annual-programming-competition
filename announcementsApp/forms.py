from django import forms
from .models import Announcement, Comment

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'info']  # Adjusted to match the model fields
        widgets = {
            'info': forms.Textarea(attrs={'rows': 5, 'cols': 40}),  # Optional: adjust rows/columns for info field
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']  # Adjusted to match the model field
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 2, 'cols': 40}),  # Optional: adjust rows/columns for comments
        }
