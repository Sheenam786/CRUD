# Generated by Django 5.0.1 on 2024-05-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_main', '0005_contactform_name_alter_contactform_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('passwrd', models.CharField(max_length=100)),
            ],
        ),
    ]
