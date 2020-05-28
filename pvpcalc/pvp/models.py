from django.db import models

# Create your models here.
class Game(models.Model):
    scores_red_player = models.CharField(max_length=2, default="10")
    scores_green_player = models.CharField(max_length=2, default="10")
    nick_red_player = models.CharField(max_length=15, default="Anonim")
    nick_green_player = models.CharField(max_length=15, default="Anonim")
    status = models.CharField(max_length=20, choices=(("free", "FREE"), ("ingame", "INGAME")), default="free")

class Task(models.Model):
    task = models.CharField(max_length=25, default="0")
    answer = models.CharField(max_length=25, default="0")