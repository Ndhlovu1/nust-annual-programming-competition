from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import DirectMessage, Group, GroupMessage, Notification
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def send_direct_message(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient_id')
        content = request.POST.get('content')
        recipient = User.objects.get(id=recipient_id)
        message = DirectMessage.objects.create(sender=request.user, recipient=recipient, content=content)

        # Send email notification
        send_mail(
            'New Message',
            f'You have received a new message: {message.content}',
            settings.DEFAULT_FROM_EMAIL,
            [recipient.email],
            fail_silently=False,
        )

        Notification.objects.create(user=recipient, message=message)
        return redirect('messagesApp:inbox')

    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messages/send_message.html', {'users': users})

@login_required
def inbox(request):
    messages = DirectMessage.objects.filter(recipient=request.user)
    return render(request, 'messages/inbox.html', {'messages': messages})

@login_required
def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('name')
        group = Group.objects.create(name=group_name)
        group.members.add(request.user)  # Add creator as the first member
        return redirect('messagesApp:groups')

    return render(request, 'messages/create_group.html')

@login_required
def send_group_message(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        group_message = GroupMessage.objects.create(group=group, sender=request.user, content=content)

        for member in group.members.all():
            send_mail(
                'New Group Message',
                f'New message in {group.name}: {group_message.content}',
                settings.DEFAULT_FROM_EMAIL,
                [member.email],
                fail_silently=False,
            )
        return redirect('messagesApp:group_detail', group_id=group_id)

    return render(request, 'messages/send_group_message.html', {'group': group})

@login_required
def add_member_to_group(request, group_id):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        group = Group.objects.get(id=group_id)
        group.members.add(user)
        return redirect('messagesApp:group_detail', group_id=group.id)

@login_required
def remove_member_from_group(request, group_id):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        group = Group.objects.get(id=group_id)
        group.members.remove(user)
        return redirect('messagesApp:group_detail', group_id=group.id)

@login_required
def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    return render(request, 'messages/group_detail.html', {'group': group})

@staff_member_required
def mass_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        recipient_ids = request.POST.getlist('recipients')
        recipients = User.objects.filter(id__in=recipient_ids)

        for recipient in recipients:
            message = DirectMessage.objects.create(sender=request.user, recipient=recipient, content=content)
            send_mail(
                'Mass Message',
                f'You have received a new mass message: {message.content}',
                settings.DEFAULT_FROM_EMAIL,
                [recipient.email],
                fail_silently=False,
            )
            Notification.objects.create(user=recipient, message=message)

        return redirect('admin:index')  # Redirect to the admin dashboard or another page

    users = User.objects.all()
    return render(request, 'messages/mass_message.html', {'users': users})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'messages/notifications.html', {'notifications': notifications})

@login_required
def mark_notification_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.is_read = True
    notification.save()
    return redirect('messagesApp:notifications')

@login_required
def reply_to_message(request, message_id):
    original_message = DirectMessage.objects.get(id=message_id)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        reply_message = DirectMessage.objects.create(
            sender=request.user,
            recipient=original_message.sender,  # Replying to the original sender
            content=content
        )

        # Optionally, you can send an email notification to the original sender
        send_mail(
            'New Reply',
            f'You have received a reply: {reply_message.content}',
            settings.DEFAULT_FROM_EMAIL,
            [original_message.sender.email],
            fail_silently=False,
        )

        return redirect('messagesApp:inbox')  # Redirect back to the inbox

    return render(request, 'messages/reply_to_message.html', {'message': original_message})



@login_required
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'messages/group_list.html', {'groups': groups})

