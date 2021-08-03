from django.test import TestCase
from django.urls import reverse
from .models import Assunto


class AssuntoTests(TestCase):

    def setUp(self):
        self.assunto = Assunto.objects.create(
            nome = 'Teste de assunto',
            situacao = 'A'
        )

    def test_assunto_listing(self):
        self.assertEqual(f'{self.assunto.nome}', 'Teste de assunto')
        self.assertEqual(f'{self.assunto.situacao}', 'A')

    def test_assunto_list_view(self):
        response = self.client.get(reverse('assuntos_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teste de')
        self.assertTemplateUsed(response, 'assuntos/assunto_list.html')
