# Generated by Django 4.2.6 on 2023-11-08 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='about',
            name='mid_name',
        ),
        migrations.RemoveField(
            model_name='about',
            name='telegram',
        ),
        migrations.RemoveField(
            model_name='about',
            name='yourwork',
        ),
    ]
