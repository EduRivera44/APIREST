# Generated by Django 4.2.5 on 2023-12-27 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0006_reparacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='salario',
            field=models.IntegerField(default=0),
        ),
    ]
