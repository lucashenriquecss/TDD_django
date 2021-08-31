from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModel(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal ='Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico ='Não'
        )

    def test_animal_cadastrado(self):
        """teste verifica se o animal esta cadastrado"""

        self.assertEqual(self.animal.nome_animal,'Leão')