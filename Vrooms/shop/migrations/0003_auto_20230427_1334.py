# Generated by Django 2.2.16 on 2023-04-27 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dop1', models.CharField(db_index=True, max_length=20)),
                ('dop2', models.CharField(db_index=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='dop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.Dop'),
        ),
    ]
