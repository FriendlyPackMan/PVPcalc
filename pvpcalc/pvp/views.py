from django.shortcuts import render
from .models import Game, Task

# Create your views here.
def home(request):
    games_list = Game.objects.all()
    return render(request, 'pvp/home.html', {'games_list': games_list})

def game(request, id, nick):
    tasks_list = Task.objects.all()
    game = Game.objects.get(id=id)
    game.nick_green_player = nick
    return render(request, 'pvp/game.html', {'tasks_list': tasks_list, 'game': game})

def loser(request):
    return render(request, 'pvp/loser.html')

def winner(request):
    return render(request, 'pvp/winner.html')