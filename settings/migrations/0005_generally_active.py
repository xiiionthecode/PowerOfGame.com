# Generated by Django 4.2.3 on 2023-07-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_rename_update_at_generally_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generally',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
