# Generated by Django 5.0.4 on 2024-05-16 06:06

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file1', models.FileField(upload_to=pathlib.PureWindowsPath('C:/Users/bj/Desktop/pbl1/media'))),
            ],
        ),
    ]