from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('game/<int:id>/<nick>/<color>', views.game, name="game"),
    path('loser/', views.loser, name="loser"),
    path('winner/', views.winner, name="winner"),
]