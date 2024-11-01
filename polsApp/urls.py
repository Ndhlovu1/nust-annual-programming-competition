# polls/urls.py

from django.urls import path
from .views import poll_list, poll_vote

app_name = 'polls'

urlpatterns = [
    path('', poll_list, name='poll_list'),
    path('vote/<int:poll_id>/', poll_vote, name='poll_vote'),
]
