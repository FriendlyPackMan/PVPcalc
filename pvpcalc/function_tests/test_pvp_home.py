from selenium import webdriver
from pvp.models import Game, Task
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestPvpHomePage(StaticLiveServerCase):

    def setUp():
        self.browser =  webdriver.Chrome('function_tests/chtomedriver.exe')
    
    def test_foo():
        pass