# Generated by Django 4.0.6 on 2022-08-12 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0020_alter_prestamo_options_alter_tarjeta_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuenta',
            old_name='tipo_id',
            new_name='tipo',
        ),
    ]