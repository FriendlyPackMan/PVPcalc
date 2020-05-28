from django.shortcuts import render
from .models import Game, Task

# Create your views here.
def home(request):
    games_list = Game.objects.all()
    return render(request, 'pvp/home.html', {'games_list': games_list})

def game(request):
    tasks_list = Game.objects.all()
    return render(request, 'pvp/game.html', {'tasks_list': tasks_list})