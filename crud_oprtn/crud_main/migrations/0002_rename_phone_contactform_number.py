# Generated by Django 5.0.6 on 2024-05-15 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='phone',
            new_name='number',
        ),
    ]
