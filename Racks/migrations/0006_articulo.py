# Generated by Django 4.1.7 on 2023-05-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Racks', '0005_delete_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Articulos',
            },
        ),
    ]
