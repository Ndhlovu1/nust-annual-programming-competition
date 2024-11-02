# accounts/admin.py
from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'location')
    search_fields = ('user__username', 'status', 'location')
    list_filter = ('status',)
