# accounts/forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'location',
            'preferred_programming_language',
            'past_participation',
            'cellphone_number',
            'mentor_name',
            'mentor_email',
            'mentor_cellphone',
            'status'
        ]
        widgets = {
            'past_participation': forms.RadioSelect,  # Display Yes/No as radio buttons
        }
