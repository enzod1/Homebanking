# Generated by Django 4.0.6 on 2022-08-12 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0005_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente_temp',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField()),
                ('branch_id', models.IntegerField()),
                ('tipo_id', models.IntegerField()),
                ('direccion_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
