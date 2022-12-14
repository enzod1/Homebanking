# Generated by Django 4.0.6 on 2022-08-12 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0006_cliente_temp_delete_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField()),
                ('branch_id', models.IntegerField()),
                ('tipo_id', models.IntegerField()),
                ('direccion_id', models.IntegerField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.authuser')),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.DeleteModel(
            name='Cliente_temp',
        ),
    ]
