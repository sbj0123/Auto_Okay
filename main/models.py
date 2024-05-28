import os

from django.db import models

from pbl1 import settings

def get_upload_path():
    # 업로드될 경로 및 파일명 반환
    path = os.path.join(settings.MEDIA_ROOT)

    if os.path.exists(path):
        os.remove(path)

    return path
class MyModel(models.Model):
    audio_file1 = models.FileField(upload_to="",null=True, blank=True )

