from django.contrib import admin
from .models import DirectMessage, Group, GroupMessage, Notification

admin.site.register(DirectMessage)
admin.site.register(Group)
admin.site.register(GroupMessage)
admin.site.register(Notification)
