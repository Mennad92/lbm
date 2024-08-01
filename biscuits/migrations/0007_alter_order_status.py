# Generated by Django 5.0.7 on 2024-08-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biscuits', '0006_alter_order_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('WAITING_FOR_PAYMENT', 'Waiting for Payment'), ('WAITING_FOR_EXPEDITION', 'Waiting for Expedition'), ('IN_DELIVERY', 'In Delivery'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='WAITING_FOR_PAYMENT', max_length=50),
        ),
    ]
