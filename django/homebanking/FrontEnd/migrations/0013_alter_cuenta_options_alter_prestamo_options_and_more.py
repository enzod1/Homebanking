# Generated by Django 4.0.6 on 2022-08-12 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0012_rename_cliente_temp_cliente_alter_cliente_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuenta',
            options={},
        ),
        migrations.AlterModelOptions(
            name='prestamo',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tarjeta',
            options={},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='branch_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_id',
            field=models.IntegerField(default=1),
        ),
    ]
