from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from apps.core.validators import validate_data_nascimento
from cpf_field.forms import CPFFieldForm
from cnpj_field.forms import CNPJFieldForm


class InteressadoForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        max_length=100,
        required=True,
    )

    nome_social = forms.CharField(
        label="Nome Social",
        max_length=100,
        required=False,
    )

    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        validators=[validate_data_nascimento],
        required=False
    )

    cpf = CPFFieldForm(
        label_suffix="CPF",
    )

    cnpj = CNPJFieldForm(
        label_suffix="CNPJ",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_interessadoForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
