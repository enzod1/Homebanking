# Generated by Django 4.0.6 on 2022-08-12 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0019_alter_cliente_options_alter_prestamo_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestamo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tarjeta',
            options={'managed': False},
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='tipo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.tipocuenta'),
        ),
    ]
