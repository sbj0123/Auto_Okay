import os
import soundfile as sf
import librosa
from django.conf import settings
from django.shortcuts import render
import numpy as np
import audioread
from core.core import get_auto_ok_instance, save_auto_ok_instance, AutoOk
from django.conf import settings

# Create your views here.

def check(request):
    auto_ok = AutoOk()
    auto_ok.set_bgm('media/MR_file.wav')
    auto_ok.get_waveform('bgm')
    auto_ok.set_vocal('media/recording.wav')
    auto_ok.analyze()
    auto_ok.get_shifted_wav()
    auto_ok.get_waveform('vocal')
    auto_ok.get_waveform('pitch')

    # auto_ok = get_auto_ok_instance(request)
    # auto_ok.set_vocal('media/recording.wav')
    # auto_ok.get_waveform('vocal')
    # auto_ok.get_waveform('pitch')
    # auto_ok.analyze()
    # shift = auto_ok.get_shifted_wav()
    # save_auto_ok_instance(request, auto_ok)

    # if request.method == 'GET':
    #     # 업로드된 파일을 받아옵니다.
    #     file_path = os.path.join(settings.MEDIA_ROOT, 'recording.wav')
    #     # 업로드된 파일을 오디오 데이터로 읽어옵니다.
    #     audio_data, sample_rate = audioread.audio_open(file_path)
    #     print('------------------------------------------')
    #
    #     # 피치를 변경합니다.
    #     semitone_change = 10 # 예시로 2 세미톤만큼 피치를 변경합니다.
    #     y_shifted = raise_pitch(audio_data, sample_rate, semitone_change)
    #
    #     # 변경된 오디오 데이터를 WAV 파일로 저장합니다.
    #     file_path = os.path.join(settings.MEDIA_ROOT, 'output_shifted.wav')
    #     print(file_path)
    #
    #
    #     if os.path.exists(file_path):
    #         os.remove(file_path)
    #
    #     sf.write(file_path, np.ravel(y_shifted), sample_rate)

    return render(request, 'check/check.html')

# def raise_pitch(audio_data, sample_rate, semitone_change):
#     # 직접 오디오 데이터와 샘플 레이트를 받아와서 피치를 변경합니다.
#     y_shifted = librosa.effects.pitch_shift(audio_data, n_steps=semitone_change, sr=sample_rate)
#     return y_shifted

