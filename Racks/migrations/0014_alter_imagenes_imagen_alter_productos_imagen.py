# Generated by Django 4.1.7 on 2023-06-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Racks', '0013_alter_imagenes_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='imagen',
            field=models.URLField(default='https://i.postimg.cc/1549gc7Y/default-prod.png', null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.URLField(default='https://i.postimg.cc/1549gc7Y/default-prod.png', null=True),
        ),
    ]