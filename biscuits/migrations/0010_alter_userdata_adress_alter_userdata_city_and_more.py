# Generated by Django 5.0.6 on 2024-07-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biscuits', '0009_alter_userdata_phone_alter_userdata_postal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='adress',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='city',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='country',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
