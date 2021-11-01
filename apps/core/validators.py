from django.core.exceptions import ValidationError
from datetime import date


dt = date.today()


def validate_data_nascimento(value):
    # Retorna erro se a data de nascimento inserida é maior que a data atual.
    if value >= dt:
        raise ValidationError(
            '%(value)s: data de nascimento não pode ser maior que a data atual',
            params={'value': value},
        )
