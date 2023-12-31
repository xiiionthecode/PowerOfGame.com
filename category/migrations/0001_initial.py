# Generated by Django 4.2.3 on 2023-07-19 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('URL', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Devices',
                'verbose_name_plural': 'Devices',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hex_color_code', models.CharField(max_length=255)),
                ('URL', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Genres',
                'verbose_name_plural': 'Genres',
            },
        ),
    ]
