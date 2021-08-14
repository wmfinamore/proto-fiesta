from django import forms
from .models import Tramite


class TramiteForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(TramiteForm, self).__init__(*args, **kwargs)
        self.fields['processo'].disabled = True
        self.fields['orgao_destino'].disabled = True
        self.fields['data_tramite'].disabled = True
        self.fields['usuario_tramite'].disabled = True

    class Meta:
        model = Tramite
        fields = ['processo',
                  'orgao_destino',
                  'despacho',
                  'data_tramite',
                  'usuario_tramite',
                  'data_recebimento',
                  ]
        labels = {
            'processo': 'Processo',
            'orgao_destino': 'Órgão Destino',
            'despacho': 'Despacho',
            'data_tramite': 'Data Trâmite',
            'usuario_tramite': 'Usuário Trâmite',
            'data_recebimento': 'Data Recepção',
        }
