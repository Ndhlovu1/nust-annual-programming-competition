# polls/admin.py

from django.contrib import admin
from .models import Poll, Vote

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'due_date', 'created_at')

admin.site.register(Poll, PollAdmin)
admin.site.register(Vote)
