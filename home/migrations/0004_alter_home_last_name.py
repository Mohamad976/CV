# Generated by Django 4.2.6 on 2023-10-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_home_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
