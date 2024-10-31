from django.contrib import admin
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Announcement, Comment
from django.contrib.auth.models import User
from django.shortcuts import render

# Customize Announcement model in admin
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')  # Display title, user, and created date
    search_fields = ('title', 'info')  # Enable search by title and info fields
    list_filter = ('created_at', 'user')  # Optional: Filter by date and user in admin list
    readonly_fields = ('created_at',)  # Make created_at read-only
    fields = ('title', 'info', 'user', 'likes', 'created_at')  # Fields in the detail view
    actions = ['send_email']  # Register the send_email function as an action

    # Limit announcements to staff and admin users only
    def has_add_permission(self, request):
        return request.user.is_staff or request.user.is_superuser

    # Email sending function
    def send_email(self, request, queryset):
        class EmailForm(forms.Form):
            users = forms.ModelMultipleChoiceField(
                queryset=User.objects.all(),
                widget=admin.widgets.FilteredSelectMultiple("Users", is_stacked=False),
                required=True,
            )

        if 'send' in request.POST:
            form = EmailForm(request.POST)
            if form.is_valid():
                selected_users = form.cleaned_data['users']
                for announcement in queryset:
                    subject = f"New Announcement: {announcement.title}"
                    message = f"{announcement.info}\n\nPosted by: {announcement.user.username}"
                    for user in selected_users:
                        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
                self.message_user(request, "Emails sent successfully!")
                return None
        else:
            form = EmailForm()

        context = {
            'form': form,
            'opts': self.model._meta,
            'announcement_count': queryset.count(),
            'title': 'Send Email to Selected Users',
        }
        return render(request, 'admin/send_email.html', context)

    send_email.short_description = "Send Email to Selected Users"  # Description for the action

# Customize Comment model in admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'announcement', 'created_at')  # Display comment text, user, and related announcement
    search_fields = ('comment',)  # Enable search by comment text
    readonly_fields = ('created_at',)  # Make created_at read-only

# Register models with admin
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Comment, CommentAdmin)
