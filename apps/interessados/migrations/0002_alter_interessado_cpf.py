# Generated by Django 3.2.7 on 2021-09-21 01:35

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interessados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interessado',
            name='cpf',
            field=cpf_field.models.CPFField(blank=True, max_length=14, null=True, unique=True, verbose_name='cpf'),
        ),
    ]
