from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField


class CustomUser(AbstractUser):
    cpf = CPFField('cpf', blank=True, null=True, max_length=14, unique=True)
