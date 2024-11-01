# polls/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Vote
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})

@login_required
def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        choice = request.POST.get('choice')
        Vote.objects.create(poll=poll, user=request.user, choice=choice)
        return redirect('polls:poll_list')
    return render(request, 'polls/poll_vote.html', {'poll': poll})
