# Generated by Django 4.1.7 on 2023-05-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Racks', '0006_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mueble',
            name='mueble',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]