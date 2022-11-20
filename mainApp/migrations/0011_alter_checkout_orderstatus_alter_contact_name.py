# Generated by Django 4.1.1 on 2022-11-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_buyer_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='orderstatus',
            field=models.IntegerField(choices=[(0, 'Order Placed'), (1, 'Not Packed'), (2, 'Packed'), (3, 'Ready to Ship'), (4, 'Shipped'), (5, 'Out For Delivery'), (6, 'Delivered'), (7, 'Cancelled')], default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]