# Generated by Django 4.2.6 on 2023-11-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_service_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(blank=True, upload_to='About/service/'),
        ),
    ]
