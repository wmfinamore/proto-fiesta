from django import forms
from .models import Tramite


class TramiteForm(forms.ModelForm):
    data_recebimento = forms.DateField(widget=forms.widgets.TextInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(TramiteForm, self).__init__(*args, **kwargs)
        # definidos os campos que serão apenas de leitura na criação do formulário
        self.fields['processo'].disabled = True
        self.fields['despacho'].disabled = True
        self.fields['orgao_destino'].disabled = True
        self.fields['usuario_tramite'].disabled = True

    class Meta:
        model = Tramite
        fields = ['processo',
                  'orgao_destino',
                  'despacho',
                  'anexo',
                  'usuario_tramite',
                  'data_recebimento',
                  ]
        labels = {
            'processo': 'Processo',
            'orgao_destino': 'Órgão Destino',
            'despacho': 'Despacho',
            'anexo': 'Anexo',
            'usuario_tramite': 'Usuário Trâmite',
            'data_recebimento': 'Data Recepção',
        }
