# Generated by Django 2.2.16 on 2023-04-27 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_dop_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dop',
            name='product',
        ),
    ]
