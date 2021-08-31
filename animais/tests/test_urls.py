from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index


class AnimaisURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url(self): #Utiliza a view index
        """Teste se a home da aplicação utiliza a função index da view """
        request = self.factory.get('/')
        #with gerenciador de contexto
        with self.assertTemplateUsed('index.html'):
            response = index(request)          
            self.assertEqual(response.status_code, 200)
