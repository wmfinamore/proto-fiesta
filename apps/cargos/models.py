from django.db import models


class Cargo(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    classe = models.CharField(max_length=10, null=True, blank=True)
    jornada = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.classe + ' - '+self.nome
