# Generated by Django 5.0.6 on 2024-07-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biscuits', '0006_alter_userdata_adress_alter_userdata_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='adress',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='city',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='country',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
