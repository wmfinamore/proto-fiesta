from django.test import TestCase
from django.urls import reverse
from .models import Interessado


class InteressadoTest(TestCase):
    def setUp(self):
        self.interessado = Interessado.objects.create(
        nome = 'Fulano da Silva',
        nome_social = 'Fulaninho',
        cpf = '036.784.000-60',
        cnpj = '78265456000170',
        )

    # Teste de recuperação de instância da classe Interessado
    def test_interessado_listing(self):
        self.assertEqual(f'{self.interessado.nome}', 'Fulano da Silva')
        self.assertEqual(f'{self.interessado.nome_social}', 'Fulaninho')
        self.assertEqual(f'{self.interessado.cpf}', '036.784.000-60')
        self.assertEqual(f'{self.interessado.cnpj}', '78265456000170')
