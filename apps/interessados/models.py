from django.db import models
import uuid
from cpf_field.models import CPFField
from cnpj_field.models import CNPJField
from django_cryptography.fields import encrypt


class Interessado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, help_text="Nome ou Razão Social")
    nome_social = models.CharField(max_length=100, blank=True, null=True)
    cpf = encrypt(CPFField('cpf', max_length=14, blank=True, null=True, unique=True))
    cnpj = CNPJField('cnpj', max_length=14, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nome
