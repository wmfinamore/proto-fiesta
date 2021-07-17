from django.db import models
from django.urls import reverse


class Cargo(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    classe = models.CharField(max_length=10, null=True, blank=True)
    jornada = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('cargos_lista')

    def __str__(self):
        return self.classe + ' - '+self.nome
