# Generated by Django 3.2.7 on 2021-11-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interessados', '0002_alter_interessado_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='interessado',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
