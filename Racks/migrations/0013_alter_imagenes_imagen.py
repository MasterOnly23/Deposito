# Generated by Django 4.1.7 on 2023-06-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Racks', '0012_alter_imagenes_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='imagen',
            field=models.ImageField(default='img/default_prod.png', null=True, upload_to='img/img-productos'),
        ),
    ]
