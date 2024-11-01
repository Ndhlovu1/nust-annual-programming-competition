# gallery/urls.py

from django.urls import path
from .views import gallery_list, like_image, comment_image, upload_image,delete_image

app_name = 'gallery'

urlpatterns = [
    path('', gallery_list, name='gallery_list'),
    path('like/<int:image_id>/', like_image, name='like_image'),
    path('comment/<int:image_id>/', comment_image, name='comment_image'),
    path('upload/', upload_image, name='upload_image'),
    path('delete/<int:image_id>/', delete_image, name='delete_image'), 
]
