# Generated by Django 3.1.12 on 2022-05-25 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabiftttd', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='config',
            old_name='gmail_account',
            new_name='ifttt_key',
        ),
        migrations.RemoveField(
            model_name='config',
            name='gmail_passwd',
        ),
        migrations.RemoveField(
            model_name='config',
            name='json_data_base',
        ),
    ]
