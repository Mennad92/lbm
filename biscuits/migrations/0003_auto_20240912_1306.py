# Generated by Django 3.2.20 on 2024-09-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biscuits', '0002_alter_productdata_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdata',
            name='product',
        ),
        migrations.AddField(
            model_name='productdata',
            name='product_id',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
