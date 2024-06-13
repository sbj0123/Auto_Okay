from django.shortcuts import render
from core.core import get_auto_ok_instance, save_auto_ok_instance, AutoOk

# Create your views here.
def download(request):

    auto_ok = AutoOk()
    auto_ok.set_bgm('media/MR_file.wav')
    auto_ok.get_waveform('bgm')
    auto_ok.set_vocal('media/recording.wav')
    auto_ok.get_waveform('vocal')
    auto_ok.get_waveform('pitch')
    auto_ok.analyze()
    shift = auto_ok.get_shifted_wav()
    auto_ok.final_song()
    auto_ok.get_waveform('pitch_bgm')

    # auto_ok = get_auto_ok_instance(request)
    # auto_ok.get_waveform('bgm')
    # shift = auto_ok.get_shifted_wav()
    # save_auto_ok_instance(request, auto_ok)
    return render(request, 'download/download.html', {'shift': shift})