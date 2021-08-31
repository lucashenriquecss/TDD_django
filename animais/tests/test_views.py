from django.http import response
from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestcase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal=Animal.objects.create(
            nome_animal ='macaco',
            predador = 'Não',
            venenoso = 'Não',
            domestico ='Não'
        )

    def test_index_view_retorna_animal(self):
        """Teste que verifica se a index retorna as caracteristicas do animal"""
        response = self.client.get('/', 
        {'buscar':'macaco'}
        )

        self.assertIs(type(response.context['caracteristicas']), QuerySet)