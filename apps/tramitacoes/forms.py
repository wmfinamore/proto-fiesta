from django import forms
from .models import Tramite
from tinymce.widgets import TinyMCE


class TramiteForm(forms.ModelForm):
    data_recebimento = forms.DateField(widget=forms.widgets.NumberInput(attrs={'type': 'date'}))
    despacho = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

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
                  'usuario_tramite',
                  'data_recebimento',
                  ]
        labels = {
            'processo': 'Processo',
            'orgao_destino': 'Órgão Destino',
            'despacho': 'Despacho',
            'usuario_tramite': 'Usuário Trâmite',
            'data_recebimento': 'Data Recepção',
        }
