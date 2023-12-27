# Generated by Django 4.2.5 on 2023-12-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0003_categoria_pelicula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ingresos_arriendo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]