# Generated by Django 4.0.6 on 2022-08-12 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0003_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]