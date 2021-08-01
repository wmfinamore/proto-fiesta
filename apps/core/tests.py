from django.test import SimpleTestCase
from django.urls import reverse


class IndexTests(SimpleTestCase):

    # Teste de resposta a rota da homepage
    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Teste de resposta ao nome da rota para a homepage
    def test_index_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
