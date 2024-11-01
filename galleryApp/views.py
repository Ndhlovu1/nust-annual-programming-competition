# gallery/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Image, Comment
from .forms import CommentForm, ImageForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def gallery_list(request):
    image_list = Image.objects.all()
    return render(request, 'gallery/gallery_list.html', {'images': image_list})

@login_required
def like_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.likes += 1  # Increment the likes count
    image.save()
    return redirect('gallery:gallery_list')

@login_required
def comment_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = image
            comment.save()
            return redirect('gallery:gallery_list')
    else:
        form = CommentForm()
    return render(request, 'gallery/comment_image.html', {'form': form, 'image': image})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = request.user
            image.save()
            return redirect('gallery:gallery_list')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload_image.html', {'form': form})

@login_required
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.user != image.owner:
        return HttpResponseForbidden("You are not allowed to delete this image.")
    
    image.delete()  # Delete the image
    return redirect('gallery:gallery_list')

