# Generated by Django 5.0.6 on 2024-08-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biscuits', '0007_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(related_name='products', to='biscuits.ingredient'),
        ),
    ]
