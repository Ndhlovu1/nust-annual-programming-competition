from django.urls import path
from .views import (
    send_direct_message,
    inbox,
    create_group,
    send_group_message,
    add_member_to_group,
    remove_member_from_group,
    group_detail,
    mass_message,
    notifications,
    mark_notification_as_read,
    reply_to_message,
)

app_name = "messagesApp"

urlpatterns = [
    path('send/', send_direct_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
    path('create_group/', create_group, name='create_group'),
    path('send_group/<int:group_id>/', send_group_message, name='send_group_message'),
    path('group/<int:group_id>/', group_detail, name='group_detail'),
    path('group/<int:group_id>/add_member/', add_member_to_group, name='add_member_to_group'),
    path('group/<int:group_id>/remove_member/', remove_member_from_group, name='remove_member_from_group'),
    path('mass_message/', mass_message, name='mass_message'),
    path('notifications/', notifications, name='notifications'),
    path('notifications/mark/<int:notification_id>/', mark_notification_as_read, name='mark_notification_as_read'),
    path('reply/<int:message_id>/', reply_to_message, name='reply_to_message'),  # New reply URL
]
