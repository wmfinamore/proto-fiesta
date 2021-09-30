from django.test import TestCase
from django.urls import reverse
from .models import Processo
from apps.assuntos.models import Assunto
from django.contrib.auth import get_user_model
from apps.interessados.models import Interessado


class ProcessoTests(TestCase):
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

    # Teste para criação e recuperação de instância da classe Processo
    def test_processo_listing(self):
        self.assertEqual(f'{self.processo.interessado.nome}', 'Cara do Teste')
        self.assertEqual(f'{self.processo.assunto.nome}', 'Teste de assunto')
        self.assertEqual(f'{self.processo.resumo}', 'Teste unitário')
        self.assertEqual(f'{self.processo.situacao}', 'A')
        self.assertEqual(f'{self.usuario_criacao.email}', 'email@email.com')

    # Teste de resposta da rota para lista de processos
    def test_processo_list_view(self):
        response = self.client.get(reverse('processos_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/2021')
        self.assertTemplateUsed(response, 'processos/processo_list.html')
