# events/views.py
# events/views.py
from django.shortcuts import get_object_or_404, render, redirect  # Added render
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Added messages for success feedback
from django.views import View
from .models import Event, RSVP

class EventListView(View):
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'events/event_list.html', {'events': events})

@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    RSVP.objects.get_or_create(event=event, user=request.user)
    messages.success(request, f"You have successfully RSVP'd to {event.title}.")
    return redirect('eventsApp:event_list')
