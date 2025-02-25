"""
URL configuration for NPCProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "NPC | COMMUNITY ADMINISTRATION"
admin.site.site_title = "NUST PROGRAMMING COMPETITION COMMUNITY"
admin.site.index_title = "NPCC MANAGEMENT SYSTEM"

urlpatterns = [
    path('account/', include('allauth.urls')),  # Adds allauth's URL routes
    path('admin/', admin.site.urls),
    path('',include('landingApp.urls')),
    path('announcements/',include('announcementsApp.urls')),
    path('forum/',include('forumApp.urls')),
    path('gallery/',include('galleryApp.urls')),
    path('archives/',include('archivesApp.urls')),
    path('polls/',include('polsApp.urls')),
    path('events/', include('eventsApp.urls')),
    path('chat/', include('chatBotApp.urls')),
    path('messages/',include('messagesApp.urls')),
    path('account/',include('profileApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)