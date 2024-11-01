# events/admin.py
from django.contrib import admin
from .models import Event, RSVP

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    actions = ['email_attendees']

    def email_attendees(self, request, queryset):
        for event in queryset:
            event.email_attendees()
        self.message_user(request, "Emails sent to all attendees.")

    email_attendees.short_description = "Email all attendees of selected events"

@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'created_at')
