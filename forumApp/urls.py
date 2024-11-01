# main/urls.py
from django.urls import path
from . import views

app_name = "forumApp"

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/add/', views.add_question, name='add_question'),
    path('answer/<int:answer_id>/upvote/', views.upvote, name='upvote'),
    path('answer/<int:answer_id>/downvote/', views.downvote, name='downvote'),
]
