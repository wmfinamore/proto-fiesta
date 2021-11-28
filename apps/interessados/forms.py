from django import forms
from .models import Interessado
from cpf_field.forms import CPFFieldForm
from cnpj_field.forms import CNPJFieldForm
# Crispy Helper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Row


class InteressadoForm(forms.ModelForm):

    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Interessado
        fields = [
            'nome',
            'nome_social',
            'data_nascimento',
            'cpf',
            'cnpj',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Dados do Interessado',
                'nome',
                'nome_social',
                'data_nascimento',
                'cpf',
                'cnpj',
            ),
            ButtonHolder(
                Submit('submit', 'Salvar')
            )
        )
