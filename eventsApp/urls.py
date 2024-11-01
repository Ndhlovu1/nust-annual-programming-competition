from django.urls import path
from .views import EventListView, rsvp_event


urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('rsvp/<int:event_id>/', rsvp_event, name='rsvp_event'),
]
