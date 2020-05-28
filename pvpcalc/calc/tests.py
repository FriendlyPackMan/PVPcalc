from django.test import SimpleTestCase, TestCase, Client
from django.urls import resolve, reverse

from .views import calc

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_calc_url_resolves(self):
        url = reverse('calc')
        self.assertEquals(resolve(url).func, calc)

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.calc_url = reverse('calc')

    def test_calc_GET(self):
        response = self.client.get(self.calc_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'calc/main.html')
