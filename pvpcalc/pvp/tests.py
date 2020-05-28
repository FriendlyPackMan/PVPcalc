from django.test import SimpleTestCase, TestCase, Client
from django.urls import resolve, reverse

from .views import home, game, loser, winner
from .models import Game

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_game_url_resolves(self):
        url = reverse('game', args=['1', 'nick'])
        self.assertEquals(resolve(url).func, game)

    def test_loser_url_resolves(self):
        url = reverse('loser')
        self.assertEquals(resolve(url).func, loser)

    def test_winner_url_resolves(self):
        url = reverse('winner')
        self.assertEquals(resolve(url).func, winner)

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        Game.objects.create()
        self.home_url = reverse('home')
        self.game_url = reverse('game', args=['1', 'nick'])
        self.loser_url = reverse('loser')
        self.winner_url = reverse('winner')

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pvp/home.html')

    def test_game_GET(self):
        response = self.client.get(self.game_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pvp/game.html')

    def test_loser_GET(self):
        response = self.client.get(self.loser_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pvp/loser.html')

    def test_winner_GET(self):
        response = self.client.get(self.winner_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pvp/winner.html')