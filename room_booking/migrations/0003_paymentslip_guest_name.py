# Generated by Django 5.0 on 2024-02-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_booking', '0002_paymentslip_booking_alter_booking_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentslip',
            name='guest_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
