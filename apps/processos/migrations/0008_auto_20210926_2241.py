# Generated by Django 3.2.7 on 2021-09-27 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0007_historicalprocesso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalprocesso',
            name='interessado',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='interessado',
        ),
    ]
