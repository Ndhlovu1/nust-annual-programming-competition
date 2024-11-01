from django.urls import path
from .views import EventListView, rsvp_event

app_name = "eventsApp"

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('rsvp/<int:event_id>/', rsvp_event, name='rsvp_event'),
]
