# Generated by Django 4.2.6 on 2023-11-08 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_about_last_name_remove_about_mid_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='first_name',
        ),
    ]
