# Generated by Django 5.0.6 on 2024-05-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_main', '0004_alter_contactform_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='name',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='number',
            field=models.IntegerField(),
        ),
    ]
