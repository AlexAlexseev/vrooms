# Generated by Django 2.2.16 on 2023-04-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20230427_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dopolnenie',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='shop.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dopolneniya',
            field=models.ManyToManyField(blank=True, null=True, to='shop.Dopolnenie'),
        ),
    ]
