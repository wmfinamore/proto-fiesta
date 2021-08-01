from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import Home


class IndexTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # Teste de resposta a rota da homepage
    def test_index_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # Teste para verificar o template retornado pela rota da homepage
    def test_index_template(self):
        self.assertTemplateUsed(self.response, 'core/index.html')

    # Teste sobre o código html do template retornado
    def test_index_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be in the page.'
        )

    # Teste que verifica a view usada para resolver a rota para a homepage
    def test_index_url_resolves_home(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            Home.as_view().__name__
        )
