# Generated by Django 4.2.6 on 2023-10-26 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_home_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='name',
            new_name='first_name',
        ),
    ]
