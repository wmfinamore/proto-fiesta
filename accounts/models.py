from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomUser(AbstractUser):
    cpf = CPFField('cpf', blank=True, null=True, max_length=14, unique=True)


# signal que cria um token quando um novo usuário é criado
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs ):
    if created:
        Token.objects.create(user=instance)

