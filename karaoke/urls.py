from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.karaoke, name='karaoke'),
    path('save_audio/', views.save_audio, name='save_audio'),
    path('check/', include('check.urls')),
]
