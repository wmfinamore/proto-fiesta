from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import Vinculo
from apps.orgaos.models import Orgao
# raw_id_field admin widget
import string
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.contrib import admin


admin.autodiscover()


# class HardcodedURLForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
#     def render(self, *args, **kwargs):
#         original_render = super(HardcodedURLForeignKeyRawIdWidget,
#                                 self).render(*args, **kwargs)
#         ADMIN_ROOT_URL = "/admin/"
#         return string.replace(original_render, "../../../", ADMIN_ROOT_URL)


class VinculoForm(forms.ModelForm):
    # lotacao = TreeNodeChoiceField(queryset=Orgao.objects.all())
    # lotacao = forms.CharField(max_length=10,
    #                           widget=HardcodedURLForeignKeyRawIdWidget(
    #                               Orgao._meta.get_field("id").remote_field, admin.site
    #                           ))
    lotacao = forms.ModelChoiceField(Orgao.objects.all(),
                                     widget=ForeignKeyRawIdWidget(Vinculo._meta.get_field("lotacao").remote_field,
                                                                  admin.site))

    # Thanks https://www.ordinarycoders.com/blog/article/using-django-form-fields-and-widgets
    data_inicio = forms.DateField(widget=forms.widgets.NumberInput(attrs={'type': 'date'}))
    data_fim = forms.DateField(widget=forms.widgets.NumberInput(attrs={'type': 'date'}), required=False)

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
