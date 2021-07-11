from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
"""
    A implementação do custom user model é altamente recomendada na documentação do
    Django 3.x.
    Caso seja necessário customizar o user model no meio do projeto, será mais trabalhoso
    do que já iniciar com o custom user model antes do primeiro migrate
"""


class CustomUser(AbstractUser):
    pass
