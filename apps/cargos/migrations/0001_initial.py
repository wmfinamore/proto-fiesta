# Generated by Django 3.2.5 on 2021-07-15 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('classe', models.CharField(blank=True, max_length=10, null=True)),
                ('jornada', models.IntegerField()),
            ],
        ),
    ]
