from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/calhe/Documents/GitHub/TDD_django/chromedriver.exe')

    def tearDown(self):#fechar aba do chrome ao fazer todos od testes
        self.browser.quit()

    def open_windowbrowser(self):
        self.browser.get(self.live_server_url)

    def test_de_falha(self):
        """ Exemplo de teste de erro"""
        self.fail('Teste falhou!!')