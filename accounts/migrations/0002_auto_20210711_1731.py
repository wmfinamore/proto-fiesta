# Generated by Django 3.2.5 on 2021-07-11 20:31

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cpf',
            field=cpf_field.models.CPFField(blank=True, max_length=14, null=True, verbose_name='cpf'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='matricula',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
