import os

from django.db import models

from pbl1 import settings


# Create your models here.
def get_upload_path():
    # 업로드될 경로 및 파일명 반환
    path = os.path.join(settings.MEDIA_ROOT, 'recording.wav')

    if os.path.exists(path):
        os.remove(path)

    return path
class Recording(models.Model):
    audioFile = models.FileField(upload_to="", null=True, blank=True)