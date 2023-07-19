# Generated by Django 4.2.3 on 2023-07-19 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_generally_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generally',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='generally',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]