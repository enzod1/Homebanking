# Generated by Django 4.0.6 on 2022-08-13 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0026_alter_prestamo_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuditoriaCuenta',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='Direccion',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='MarcaTarjetas',
        ),
        migrations.DeleteModel(
            name='Movimientos',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Sucursal',
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='customer',
        ),
        migrations.DeleteModel(
            name='TipoCliente',
        ),
        migrations.DeleteModel(
            name='TipoOperaciones',
        ),
        migrations.DeleteModel(
            name='TipoTarjeta',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Cuenta',
        ),
        migrations.DeleteModel(
            name='Prestamo',
        ),
        migrations.DeleteModel(
            name='Tarjeta',
        ),
        migrations.DeleteModel(
            name='TipoCuenta',
        ),
    ]
