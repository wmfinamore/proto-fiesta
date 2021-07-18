from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Cargo(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    classe = models.CharField(max_length=10, null=True, blank=True)
    jornada = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('cargos_lista')

    def __str__(self):
        return self.classe + ' - '+self.nome


class Vinculo(models.Model):
    funcionario = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    matricula = models.PositiveIntegerField(unique=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    @property
    def nome_completo(self):
        return self.funcionario.get_full_name()

    def __str__(self):
        return self.funcionario.get_full_name() + '-' + self.cargo.nome
