# Generated by Django 4.2.3 on 2023-07-19 03:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generally',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='update_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]