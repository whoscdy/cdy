# Generated by Django 2.2.7 on 2019-11-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]
