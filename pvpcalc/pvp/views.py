from django.shortcuts import render
from .models import Game, Task

# Create your views here.
def home(request):
    games_list = Game.objects.all()
    max_id = 1 + Game.objects.values_list('id', flat=True).order_by('id').reverse()[0]
    return render(request, 'pvp/home.html', {'games_list': games_list, 'max_id': max_id})

def game(request, id, nick, color):
    tasks_list = Task.objects.all()
    if Game.objects.filter(id=id).exists():
        game = Game.objects.get(id=id)
        game.nick_green_player = nick
        game.status = "INGAME"
    else:
        game = Game.objects.create()
        game.nick_red_player = nick
        game.save()

    return render(request, 'pvp/game.html', {'tasks_list': tasks_list, 'game': game})

def loser(request):
    return render(request, 'pvp/loser.html')

def winner(request):
    return render(request, 'pvp/winner.html')