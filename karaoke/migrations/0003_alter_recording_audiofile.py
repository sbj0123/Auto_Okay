# Generated by Django 5.0.6 on 2024-05-27 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karaoke', '0002_remove_recording_audio_file_recording_audiofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='audioFile',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]