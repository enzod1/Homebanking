# Generated by Django 4.0.6 on 2022-08-12 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0015_alter_cuenta_options_alter_prestamo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.cliente'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FrontEnd.cliente'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.cliente'),
        ),
    ]
