import subprocess
import wave

import audioread
import librosa
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
import soundfile as sf
from pydub import AudioSegment


def wav_to_mp3(wave_file_path):
    file_path = os.path.join(settings.MEDIA_ROOT, 'recording.mp3')
    if os.path.exists(file_path) :
        os.remove(file_path)
    # FFmpeg 명령 구성
    command = [
        'ffmpeg',
        '-i', wave_file_path,  # 입력 파일
        file_path  # 출력 파일
    ]

    # subprocess.run을 사용하여 명령 실행
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("FFmpeg 명령 성공:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("FFmpeg 명령 실패:", e.stderr)


@csrf_exempt
def save_audio(request):
    if request.method == 'POST' and request.FILES.get('audioFile'):
        audio_file = request.FILES['audioFile']
        file_path = os.path.join(settings.MEDIA_ROOT, 'recording.wav')

        with open(file_path, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)

        wav_to_mp3(file_path)
        return JsonResponse({'status': 'success', 'file_path': file_path})
    return JsonResponse({'status': 'failed'}, status=400)


# def save_audio(request):
#     if request.method == 'POST' and request.FILES.get('audioFile'):
#         audio_file = request.FILES['audioFile']
#         file_path = os.path.join(settings.MEDIA_ROOT, audio_file.name)
#         with open(file_path, 'wb+') as destination:
#             for chunk in audio_file.chunks():
#                 destination.write(chunk)
#         return JsonResponse({'status': 'success', 'file_path': file_path})
#     return JsonResponse({'status': 'failed'}, status=400)

def karaoke(request):
    if request.method == 'POST':
        # 업로드된 파일을 받아옵니다.
        file_path = os.path.join(settings.MEDIA_ROOT, 'recording.mp3')
        audio = AudioSegment.from_mp3(file_path)
        output_path = os.path.join(settings.MEDIA_ROOT, 'recording.wav')
        if os.path.exists(output_path):
            os.remove(output_path)
        audio.export(output_path, format='wav')
        # 업로드된 파일을 오디오 데이터로 읽어옵니다.
        audio_data, sample_rate = librosa.load(output_path, sr=None)

        # 피치를 변경합니다.
        semitone_change = 3
        y_shifted = raise_pitch(audio_data, sample_rate, semitone_change)

        # 변경된 오디오 데이터를 WAV 파일로 저장합니다.
        output_path = os.path.join(settings.MEDIA_ROOT, 'output_shifted.wav')
        print(file_path)

        if os.path.exists(output_path):
            os.remove(output_path)

        sf.write(output_path, y_shifted, sample_rate)
        return redirect('check')
    return render(request, 'karaoke/karaoke.html')


def raise_pitch(audio_data, sample_rate, semitone_change):
    # 직접 오디오 데이터와 샘플 레이트를 받아와서 피치를 변경합니다.
    return librosa.effects.pitch_shift(audio_data, n_steps=semitone_change, sr=sample_rate)

