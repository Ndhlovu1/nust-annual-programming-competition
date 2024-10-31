# announcements/urls.py

from django.urls import path
from .views import announcement_list, like_announcement, add_comment

app_name = 'announcementsApp'

urlpatterns = [
    path('', announcement_list, name='announcements'),  # Show announcements
    path('like/<int:pk>/', like_announcement, name='like_announcement'),
    path('comment/<int:pk>/', add_comment, name='add_comment'),
]
