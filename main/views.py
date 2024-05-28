import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from pydub import AudioSegment

from main.forms import MyModelForm
from pbl1 import settings


# # Create your views here.
# def index(request):
#     if request.method == 'POST':
#         my_file = request.FILES['file']
#         MyFile.objects.create(my_file=my_file)
#     return render(request, 'main/main.html')

def upload_file(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        request.FILES['audio_file1'].name = 'MR_file.wav'
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, 'MR_file.wav')):
            os.remove(os.path.join(settings.MEDIA_ROOT, 'MR_file.wav'))
        if form.is_valid():
            form.save()
            return redirect('karaoke')  # 파일 업로드 성공 시 이동할 URL
    else:
        form = MyModelForm()
    return render(request, 'main/main.html', {'form': form})
