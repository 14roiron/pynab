# Generated by Django 3.0.7 on 2021-03-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nabweatherd', '0007_config_weather_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='weather_frequency',
            field=models.IntegerField(default=0),
        ),
    ]
