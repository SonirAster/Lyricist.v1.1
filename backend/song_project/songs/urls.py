from django.urls import path

from .views import groupAPI

urlpatterns = [
    path('', groupAPI)
]