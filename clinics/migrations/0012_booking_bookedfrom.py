# Generated by Django 2.2.6 on 2019-11-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0011_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bookedfrom',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]