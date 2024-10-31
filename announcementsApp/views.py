# announcements/views.py

from django.shortcuts import render, redirect
from .models import Announcement, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')  # Show latest announcements first
    comment_form = CommentForm()
    return render(request, 'announcements/list.html', {'announcements': announcements, 'comment_form': comment_form})

@login_required
def like_announcement(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    if request.user in announcement.likes.all():
        announcement.likes.remove(request.user)
    else:
        announcement.likes.add(request.user)
    return redirect('announcementsApp:announcements')

@login_required
def add_comment(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.announcement = announcement
            comment.save()
            return redirect('announcementsApp:announcements')
        

# announcements/views.py

from django.shortcuts import render, redirect
from .models import Announcement
from django.contrib.auth.decorators import login_required

@login_required
def like_announcement(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    if request.user in announcement.likes.all():
        announcement.likes.remove(request.user)
    else:
        announcement.likes.add(request.user)
    return redirect('announcementsApp:announcements')


