# Generated by Django 5.0.4 on 2024-05-16 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_mymodel_audio_file2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]