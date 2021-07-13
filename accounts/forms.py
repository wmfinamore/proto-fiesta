from django.contrib.auth import get_user_model
# get_user_model retorna o modelo indicado em AUTH_USER_MODEL no arquivo settings.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'cpf', 'matricula', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'cpf', 'matricula', )