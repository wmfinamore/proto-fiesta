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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # na instanciação do form não carrega os interessados no select
        self.fields['interessado'].queryset = Interessado.objects.none()
        if 'interessado' in self.data:
            # retorna o query com os dados para processar o POST
            self.fields['interessado'].queryset = Interessado.objects.all()
        elif self.instance:
            # Retorna o valor do campo interessado para Update
            self.fields['interessado'].queryset = Interessado.objects.filter(pk=self.instance.interessado.id)
