# accounts/views.py
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    profile = request.user.profile  # Access the related profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Replace with your profile URL name
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})
