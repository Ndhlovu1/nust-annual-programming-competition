from django.urls import path
from . import views

app_name = "landingApp"


urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Define the landing page URL
]