# Generated by Django 4.0.6 on 2022-08-25 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Common', '0004_alter_cliente_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='tipo_id',
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tipoCliente', to='Common.tipocliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
