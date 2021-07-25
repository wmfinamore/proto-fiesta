from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import Vinculo
from apps.orgaos.models import Orgao


class VinculoForm(forms.ModelForm):
    lotacao = TreeNodeChoiceField(queryset=Orgao.objects.all())

    class Meta:
        model = Vinculo
        fields = ['funcionario', 'cargo', 'matricula', 'lotacao', 'data_inicio', 'data_fim']
        labels = {
            'funcionario': 'Funcionário',
            'cargo': 'Cargo',
            'matricula': 'Matrícula',
            'lotacao': 'Lotação',
            'data_inicio': 'Data de Admissão',
            'data_fim': 'Data de Demissão',
        }
        widgets = {
            'data_inicio': forms.SelectDateWidget,
            'data_fim': forms.SelectDateWidget,
        }
