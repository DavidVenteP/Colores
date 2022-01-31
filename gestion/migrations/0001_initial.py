# Generated by Django 3.2.9 on 2022-01-31 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colors_Inventory',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False, verbose_name='Código')),
                ('name', models.CharField(max_length=200, verbose_name='Color')),
                ('quantity', models.IntegerField(default=0, verbose_name='Cantidad')),
            ],
            options={
                'verbose_name': 'Inventario del color',
                'verbose_name_plural': 'Inventario de colores',
            },
        ),
    ]