from django import forms
from .models import Processo
from apps.interessados.models import Interessado
from apps.assuntos.models import Assunto


class SearchForm(forms.Form):
    query = forms.CharField(label='Pesquisa')


class ProcessoForm(forms.ModelForm):

    class Meta:
        model = Processo
        fields = ['interessado', 'assunto', 'resumo', 'anexo', 'situacao', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.initial and 'interessado' not in self.data:
            self.fields['interessado'].queryset = Interessado.objects.none()
            self.fields['assunto'].queryset = Assunto.objects.none()
        # na instanciação do form não carrega os interessados no select
        else:
            if 'interessado' in self.data:
                # retorna o query com os dados para processar o POST
                self.fields['interessado'].queryset = Interessado.objects.all()
                self.fields['assunto'].queryset = Assunto.objects.all()
            elif self.instance:
                # Retorna o valor do campo interessado para Update
                self.fields['interessado'].queryset = Interessado.objects.filter(pk=self.instance.interessado.id)
                self.fields['assunto'].queryset = Assunto.objects.filter(pk=self.instance.assunto.id)
