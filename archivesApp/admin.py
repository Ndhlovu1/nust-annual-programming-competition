# archive/admin.py
from django.contrib import admin
from .models import Book, Rating

admin.site.register(Book)
admin.site.register(Rating)
