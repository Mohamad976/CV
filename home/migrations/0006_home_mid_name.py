# Generated by Django 4.2.6 on 2023-10-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_name_home_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='mid_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
