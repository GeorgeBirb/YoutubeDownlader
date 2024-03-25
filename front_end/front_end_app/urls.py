# front_end_app/urls.py
from django.urls import path
from .views import ytDownloader_view

urlpatterns = [
    path('ytDownloader/', ytDownloader_view, name='ytDownloader'),
]
