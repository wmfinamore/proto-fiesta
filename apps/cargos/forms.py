from django import forms
from .models import Vinculo


class VinculoForm(forms.ModelForm):

    class Meta:
        model = Vinculo
        fields = ['funcionario', 'cargo', 'matricula', 'data_inicio', 'data_fim']
        labels = {
            'funcionario': 'Funcionário',
            'cargo': 'Cargo',
            'matricula': 'Matrícula',
            'data_inicio': 'Data de Admissão',
            'data_fim': 'Data de Demissão',
        }
        widgets = {
            'data_inicio': forms.SelectDateWidget,
            'data_fim': forms.SelectDateWidget,
        }
