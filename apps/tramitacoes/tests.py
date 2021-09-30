from django.test import TestCase
from django.urls import reverse
from .models import Tramite
from apps.processos.models import Processo
from apps.orgaos.models import Orgao
from apps.assuntos.models import Assunto
from django.contrib.auth import get_user_model
from apps.interessados.models import Interessado


class TramiteTests(TestCase):
    def setUp(self):
        self.assunto = Assunto.objects.create(
            nome='Teste de assunto',
            situacao='A'
        )

        Usuario = get_user_model()
        self.usuario_criacao = Usuario.objects.create(
            username='will',
            email='email@email.com',
            password='A12345678a'
        )

        self.interessado = Interessado.objects.create(
            nome='Cara do Teste',
            nome_social='Carinha',
            cpf='965.814.590-62',
            cnpj='27170985000150',
        )

        self.processo = Processo.objects.create(
            interessado=self.interessado,
            assunto=self.assunto,
            resumo='Teste unitário',
            situacao='A',
            usuario_criacao=self.usuario_criacao
        )

        self.orgao = Orgao.objects.create(
            nome='Secretaria de Tecnologia da Informação',
            sigla='SETI',
            tipo='F',
            situacao='A',
        )

        self.tramite = Tramite.objects.create(
            processo=self.processo,
            orgao_destino=self.orgao,
            despacho='Segue para teste de tramitação',
            usuario_tramite=self.usuario_criacao
        )

    # Teste para criação e recuperação de instaância da classe Tramite
    def test_tramite_listing(self):
        self.assertEqual(f'{self.tramite.processo.resumo}', 'Teste unitário')
        self.assertEqual(f'{self.tramite.orgao_destino.sigla}', 'SETI')
        self.assertEqual(f'{self.tramite.despacho}', 'Segue para teste de tramitação')
        self.assertEqual(f'{self.tramite.usuario_tramite.email}', 'email@email.com')
