# Generated by Django 5.2 on 2025-05-07 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_storage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='path',
        ),
    ]
