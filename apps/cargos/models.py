from django.db import models


class Cargos(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    classe = models.CharField(max_length=10, null=True, blank=True)
    jornada = models.IntegerField()

    def __str__(self):
        return self.classe + ' - '+self.nome
