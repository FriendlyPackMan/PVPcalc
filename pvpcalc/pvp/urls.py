from django.contrib import admin
from django.urls import path

from pvp import views

urlpatterns = [
    path('', views.home),
]