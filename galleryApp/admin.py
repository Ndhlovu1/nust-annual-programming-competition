# gallery/admin.py

from django.contrib import admin
from .models import Image, Comment

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'likes')  # Fields to display in the admin list view
    search_fields = ('title', 'description')  # Fields to search
    list_filter = ('owner', 'created_at')  # Filter options in the admin

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'created_at')  # Fields to display in the admin list view
    search_fields = ('user__username', 'image__title', 'text')  # Fields to search
    list_filter = ('user', 'image')  # Filter options in the admin
