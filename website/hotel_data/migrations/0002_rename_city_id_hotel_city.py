# Generated by Django 3.2.12 on 2022-02-21 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='city_id',
            new_name='city',
        ),
    ]
