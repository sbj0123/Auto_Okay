# Generated by Django 5.0.4 on 2024-05-16 06:17

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='audio_file1',
            field=models.FileField(upload_to=(pathlib.PureWindowsPath('C:/Users/bj/Desktop/pbl1/media'), 'audio_file1')),
        ),
    ]
