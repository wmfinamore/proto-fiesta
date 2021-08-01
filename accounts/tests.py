from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    # Teste para criação de usuários
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='email@email.com',
            password='A12345678a'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'email@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # Teste para criação de superuser
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superemail@email.com',
            password='A12345678a'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superemail@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
