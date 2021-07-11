from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField
from django.db import models


class CustomUser(AbstractUser):
    cpf = CPFField('cpf', blank=True, null=True, max_length=14)
    matricula = models.CharField(max_length=8, blank=True, null=True)
