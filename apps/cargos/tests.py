from django.test import TestCase
from .models import Cargo, Vinculo
from apps.orgaos.models import Orgao
from django.contrib.auth import get_user_model
from django.urls import reverse


# Teste de criação e recuperação de instancia de Cargo
class CargoTests(TestCase):
    def setUp(self):
        self.cargo = Cargo.objects.create(
            nome='Tester',
            classe='TS16',
            jornada=30,
        )

    def test_cargo_listing(self):
        self.assertEqual(f'{self.cargo.nome}', 'Tester')
        self.assertEqual(f'{self.cargo.classe}', 'TS16')
        self.assertEqual(self.cargo.jornada, 30)

    def test_cargo_list_view(self):
        response = self.client.get(reverse('cargos_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tester')
        self.assertTemplateUsed(response, 'cargos/cargo_list.html')

# Teste de criação e recuperação de instancia de vinculo
class VinculoTests(TestCase):
    def setUp(self):
        self.cargo = Cargo.objects.create(
            nome='Tester',
            classe='TS16',
            jornada=30,
        )
        User = get_user_model()
        self.user = User.objects.create_user(
            username='will',
            email='email@email.com',
            password='A12345678a'
        )
        self.orgao = Orgao.objects.create(
            nome='Secretaria1',
            sigla='SEC',
            tipo='F',
            situacao='A'
        )
        self.vinculo = Vinculo.objects.create(
            funcionario=self.user,
            cargo=self.cargo,
            matricula=555555,
            lotacao=self.orgao,
            data_inicio='2021-01-01'
        )

    def test_vinculo_list(self):
        self.assertEqual(f'{self.vinculo.funcionario.username}', 'will')
        self.assertEqual(f'{self.vinculo.cargo.nome}', 'Tester')
        self.assertEqual(self.vinculo.matricula, 555555)
        self.assertEqual(f'{self.vinculo.lotacao.nome}', 'Secretaria1')
        self.assertEqual(f'{self.vinculo.data_inicio}', '2021-01-01')

    def test_vinculo_list_view(self):
        response = self.client.get(reverse('vinculos_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 555555)
        self.assertTemplateUsed(response, 'cargos/vinculo_list.html')
