import librosa
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from core.core import AutoOk, get_auto_ok_instance, save_auto_ok_instance
import soundfile as sf
from pydub import AudioSegment
from karaoke.forms import MyModelForm


@csrf_exempt
def save_audio(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)

        if os.path.exists(os.path.join(settings.MEDIA_ROOT, 'recording.wav')):
            os.remove(os.path.join(settings.MEDIA_ROOT, 'recording.wav'))
        if form.is_valid():
            recording = form.save()
            file_path = recording.audioFile.path
            # 파일이 WAV 형식인지 확인하고 변환
            try:
                audio = AudioSegment.from_file(file_path)
                audio.export(file_path, format='wav')
                # autoK.set_vocal(audio)
                # autoK.save_to_session(request, 'autoK')
            except Exception as e:
                return JsonResponse({'status': 'failed', 'error': str(e)}, status=400)
        return redirect('check')
    return JsonResponse({'status': 'failed'}, status=400)

def karaoke(request):
    auto_ok = get_auto_ok_instance(request)
    auto_ok.set_bgm('media/MR_file.wav')
    auto_ok.get_waveform('bgm')
    save_auto_ok_instance(request, auto_ok)
    if request.method == 'POST':
        # 업로드된 파일을 받아옵니다.
        # file_path = os.path.join(settings.MEDIA_ROOT, 'recording.mp3')
        # audio = AudioSegment.from_mp3(file_path)
        file_path = os.path.join(settings.MEDIA_ROOT, 'recording.wav')
        # audio = AudioSegment.from_file(file_path)
        # audio.export(file_path, format='wav')
        # if os.path.exists(output_path):
        #     os.remove(output_path)
        # audio.export(output_path, format='wav')
        # 업로드된 파일을 오디오 데이터로 읽어옵니다.
        audio_data, sample_rate = librosa.load(file_path, sr=None)

        # 피치를 변경합니다.
        semitone_change = 3
        y_shifted = raise_pitch(audio_data, sample_rate, semitone_change)

        # 변경된 오디오 데이터를 WAV 파일로 저장합니다.
        output_path = os.path.join(settings.MEDIA_ROOT, 'output_shifted.wav')

        if os.path.exists(output_path):
            os.remove(output_path)

        sf.write(output_path, y_shifted, sample_rate)
        return redirect('check')
    return render(request, 'karaoke/karaoke.html')

def raise_pitch(audio_data, sample_rate, semitone_change):
        # 직접 오디오 데이터와 샘플 레이트를 받아와서 피치를 변경합니다.
    return librosa.effects.pitch_shift(audio_data, n_steps=semitone_change, sr=sample_rate)
