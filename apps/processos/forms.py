from django import forms
from .models import Processo
from apps.interessados.models import Interessado
from apps.assuntos.models import Assunto


class SearchForm(forms.Form):
    query = forms.CharField(label='Pesquisa')


class ProcessoForm(forms.ModelForm):

    class Meta:
        model = Processo
        fields = ['interessado', 'assunto', 'resumo', 'situacao']
