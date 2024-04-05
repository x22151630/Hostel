# Generated by Django 4.2.11 on 2024-04-05 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostel',
            old_name='image_url',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='hostel',
            old_name='place_info',
            new_name='service_info',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='best_time_to_visit',
        ),
    ]
