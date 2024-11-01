# archive/urls.py
from django.urls import path
from . import views

app_name = "archivesApp"

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('<int:pk>/download/', views.download_pdf, name='download_pdf'),
]
