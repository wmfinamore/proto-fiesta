# Generated by Django 3.2.9 on 2021-12-24 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interessados', '0004_alter_interessado_data_nascimento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interessado',
            options={'ordering': ['-id']},
        ),
    ]