# main/forms.py
from django import forms
from .models import Question, Answer, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "content", "tags", "image"]
    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add tags separated by commas'}))

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content", "image"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "image"]
