# Generated by Django 2.2.16 on 2023-04-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]