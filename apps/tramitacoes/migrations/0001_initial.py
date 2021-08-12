# Generated by Django 3.2.5 on 2021-08-12 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orgaos', '0001_initial'),
        ('processos', '0005_alter_processo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('despacho', models.TextField(blank=True, null=True)),
                ('data_tramite', models.DateTimeField(auto_now_add=True)),
                ('data_recebimento', models.DateTimeField(blank=True, null=True)),
                ('orgao_destino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orgao_tramites', to='orgaos.orgao')),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='processo_tramites', to='processos.processo')),
                ('usuario_recepcao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usuario_recepcoes', to=settings.AUTH_USER_MODEL)),
                ('usuario_tramite', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario_tramites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-data_tramite'],
            },
        ),
    ]
