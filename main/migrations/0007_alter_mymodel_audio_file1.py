# Generated by Django 5.0.6 on 2024-05-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_mymodel_audio_file1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='audio_file1',
            field=models.FileField(upload_to='media/MR_file.wav'),
        ),
    ]
