# -*- coding: utf-8 -*-
"""voice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jwcTdlAvQKvVNyAOd3AwOPasblfm-WmI
"""
import os
import pickle

from pbl1 import settings

#variable
path = './'
BGM_FILENAME = 'bgm.wav'
VOCAL_FILENAME = 'vocal.wav'


import numpy as np
import librosa
# import autochord
import matplotlib.pyplot as plt
import parselmouth
from rnnoise_wrapper import RNNoise
import soundfile

def nearnest(value, dict_in):
  near = 0
  diff = float("inf")
  for k, v in dict_in.items():
    if abs(diff) > abs(value - v):
      near = k
      diff = value - v
  return near, diff


class AutoOk:

    def __init__(self, url_bgm=None, url_vocal=None, diff=None):
        self.url_bgm = url_bgm
        self.url_vocal = url_vocal
        self.diff = diff
        self.list_pitch_diff = []

        self.dict_scale = {
            'N': [],

            'C:maj': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            'Db:maj': ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],
            'D:maj': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
            'Eb:maj': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'],
            'E:maj': ['E', 'F', 'G#', 'A', 'B', 'C#', 'D#'],
            'F:maj': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
            'Gb:maj': ['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F'],
            'G:maj': ['G', 'A', 'B', 'C', 'D', 'E', 'F'],
            'Ab:maj': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
            'A:maj': ['A', 'B', 'C#', 'D', 'E', 'F', 'G#'],
            'Bb:maj': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
            'B:maj': ['B', 'C#', 'D#', 'E', 'F', 'G#', 'A#'],

            'C:min': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
            'Db:min': ['Db', 'Eb', 'Fb', 'Gb', 'Ab', 'A', 'Cb', 'Db'],
            'D:min': ['D', 'E', 'F', 'G', 'A', 'Bb', 'C#'],
            'Eb:min': ['Eb', 'F', 'Gb', 'Ab', 'Bb', 'Cb', 'Db'],
            'E:min': ['E', 'F', 'G', 'A', 'B', 'C', 'D'],
            'F:min': ['F', 'G', 'Ab', 'A', 'C', 'Db', 'Eb'],
            'Gb:min': ['Gb', 'G#', 'A', 'B', 'C#', 'D', 'E'],
            'G:min': ['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F'],
            'Ab:min': ['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb'],
            'A:min': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            'Bb:min': ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab'],
            'B:min': ['B', 'C#', 'D', 'E', 'F', 'G', 'A']
        }

        self.dict_note_to_key = {
        'C':32.7032,
        'C#':34.6478,
        'Db':34.6478,
        'D':36.7081,
        'D#':38.8909,
        'Eb':38.8909,
        'E':41.2034,
        'Fb':43.6535,
        'F':43.6535,
        'F#':46.2493,
        'Gb':46.2493,
        'G':48.9994,
        'G#':51.9130,
        'Ab':51.9130,
        'A':55.0000,
        'A#':58.2705,
        'Bb':58.2705,
        'B':61.7354,
        'Cb':61.7354
    }

        self.octaves = [32.7032, 65.4064, 130.8128, 261.6256, 523.2511, 1046.5023, 2093.0045, 4186.009]

        self.list_shifted_vocal = []

    def to_dict(self):
        return self.__dict__
    def set_bgm(self,url):
        self.url_bgm = url
        return True

    def set_vocal(self,url):
        self.url_vocal = url
        return True

    def get_waveform(self, case):

        #case에 따라 waveform 출력값 변경
        if case == 'bgm':
            y, sr = librosa.load(self.url_bgm)
            self.image_path = 'bgm_image.png'
        if case == 'vocal':
            y, sr = librosa.load(self.url_vocal)
            self.image_path = 'vocal_image.png'

        # 음성 파일의 길이 계산 (초 단위)
        duration = librosa.get_duration(y=y, sr=sr)
        # 세로 길이를 고정하고, 가로 길이는 음성 파일의 길이에 비례하도록 설정
        fixed_height = 6  # 세로 길이 (inches)
        width_per_second = 1  # 초당 가로 길이 (inches)
        fig_width = width_per_second * duration

        plt.figure(figsize=(fig_width, fixed_height), frameon=False)
        librosa.display.waveshow(y, sr=sr)
        plt.axis("off")
        plt.xlim(0, duration)

        # 이미지 파일로 저장
        plt.savefig(self.image_path, bbox_inches='tight', pad_inches=0)

        return True

        # case에 따라 waveform 출력값 변경
        if case == 'bgm':
            y, sr = librosa.load(self.url_bgm)
            self.image_path = 'bgm_image.png'
        if case == 'vocal':
            y, sr = librosa.load(self.url_vocal)
            self.image_path = 'vocal_image.png'

        # 음성 파일의 길이 계산 (초 단위)
        duration = librosa.get_duration(y=y, sr=sr)
        # 세로 길이를 고정하고, 가로 길이는 음성 파일의 길이에 비례하도록 설정
        fixed_height = 6  # 세로 길이 (inches)
        width_per_second = 1  # 초당 가로 길이 (inches)
        fig_width = width_per_second * duration

        plt.figure(figsize=(fig_width, fixed_height))
        librosa.display.waveshow(y, sr=sr)
        plt.axis("off")
        plt.xlim(0, duration)

        # 이미지 파일로 저장
        save_path = os.path.join(settings.MEDIA_ROOT, 'MR_file.wav') + self.image_path  # 원하는 경로로 수정
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

        return True

    def analyze(self):
        snd = parselmouth.Sound(self.url_bgm)
        chords = autochord.recognize(self.url_bgm, lab_fn='chords.lab')
        pitch = snd.to_pitch()
        pitch_values = pitch.selected_array['frequency']

        for i in range(len(pitch_values)):
            # pitch_values[i] == 0: continue
            time = i / 100
            list_chord = []
            octave = 0
            for oct in range(8):
                if pitch_values[i] * 10 > self.octaves[oct]:
                    octave = oct

            for chord in chords:
                if chord[0] < time and time < chord[1]:
                    list_chord = self.dict_scale[chord[2]]
                    break

            dict_copyed_note_to_key = self.dict_note_to_key.copy()
            for k, v in dict_copyed_note_to_key.items():
                if not k in list_chord:
                    dict_copyed_note_to_key[k] = 0
                else:
                    dict_copyed_note_to_key[k] *= 2 ** octave

            self.list_pitch_diff.append([self.nearnest(pitch_values[i] * 10, dict_copyed_note_to_key), octave, pitch_values[i]])
        return True


    def get_diff_section(self):
        return self.list_pitch_diff


    def get_shifted_wav(self):
        denoiser = RNNoise()
        list_diff_by_section = []
        last_oct, last_key = 0, ''
        int_diff_sum = 0
        int_pitch_sum = 0
        int_count = 1
        start_ind = 0
        last_ind = 0

        for index, diff in enumerate(self.list_pitch_diff):
            if diff[1] == last_oct and diff[0][0] == last_key:
                int_diff_sum += diff[0][1]
                int_pitch_sum += diff[2]
                int_count += 1
                last_ind = index
            else:
                # list_diff_section = [시작idx, 끝idx, 평균 Diff, 평균 Pitch]
                list_diff_by_section.append([start_ind, last_ind, int_diff_sum / int_count, int_pitch_sum / int_count * 10])
                last_oct = diff[1]
                last_key = diff[0][0]
                int_diff_sum = 0
                int_pitch_sum = 0
                int_count = 1
                start_ind = index

        list_diff_by_section.pop(0)

        self.list_shifted_vocal = []
        song, sr = librosa.load(self.url_vocal)

        for d in list_diff_by_section:
            temp = song[d[0] * sr // 100:d[1] * sr // 100]
            if not d[2] == 0.0:
                temp = librosa.effects.pitch_shift(y=temp, sr=sr, n_steps=d[2] / d[3] * 12)
            self.list_shifted_vocal.extend(temp)
        self.list_shifted_vocal = denoiser.filter(self.list_shifted_vocal)
        
        return self.list_shifted_vocal


    def get_shifted_part_wav(self, start, end):
        self.snd
        return True

    def final_song(self):
        snd = parselmouth.Sound(self.url_bgm)
        snd = snd[:len(self.list_shifted_vocal)]

    def nearnest(self, value, dict_in):
        near = 0
        diff = float("inf")
        for k, v in dict_in.items():
            if abs(diff) > abs(value - v):
                near = k
                diff = value - v
        return near, diff

#chords = autochord.recognize(path + BGM_FILENAME, lab_fn = 'chords.lab')

#for chord in chords:
#  if chord[2] in dictScale:
#    print(chord, dictScale[chord[2]])


#snd = parselmouth.Sound(path + VOCAL_FILENAME)


# intensity = snd.to_intensity()
# spectrogram = snd.to_spectrogram()
#pitch = snd.to_pitch()
#pitch_values = pitch.selected_array['frequency']


#Pitch Difference 처리
#listPitchDiff = []

#for i in range(len(pitch_values)):
  #pitch_values[i] == 0: continue
#  time = i / 100
#  listChord = []
#  octave = 0
#  for oct in range(8):
#    if pitch_values[i] * 10 > octaves[oct]:
#      octave = oct

#  for chord in chords:
#    if chord[0] < time and time < chord[1]:
#      listChord = dictScale[chord[2]]
#      break

#  dictCopyedNoteToKey = dictNoteToKey.copy()
#  for k, v in dictCopyedNoteToKey.items():
#    if not k in listChord:
#      dictCopyedNoteToKey[k] = 0
#    else:
#      dictCopyedNoteToKey[k] *= 2 ** octave

#  listPitchDiff.append([nearnest(pitch_values[i] * 10, dictCopyedNoteToKey), octave, pitch_values[i]])


# 구간별 pitch-Shift 시
#listDiffBySection = []
#lastOct, lastKey = 0, ''
#intDiffSum = 0
#intPitchSum = 0
#intCount = 1
#startInd = 0
#lastInd = 0

#for index, diff in enumerate(listPitchDiff):
#  if diff[1] == lastOct and diff[0][0] == lastKey:
#    intDiffSum += diff[0][1]
#    intPitchSum += diff[2]
#    intCount += 1
#    lastInd = index
#  else:
    #listDiffSection = [시작idx, 끝idx, 평균 Diff, 평균 Pitch]
#    listDiffBySection.append([startInd, lastInd, intDiffSum / intCount, intPitchSum / intCount * 10])
#    lastOct = diff[1]
#    lastKey = diff[0][0]
#    intDiffSum = 0
#    intPitchSum = 0
#    intCount = 1
#    startInd = index

#listDiffBySection.pop(0)

# 여기서부터 Pitch-Shift
#listShifted_vocal = []
#song, sr = librosa.load(path + VOCAL_FILENAME)

#for d in listDiffBySection:
#  temp = song[d[0] * sr // 100:d[1] * sr // 100]
#  if not d[2] == 0.0:
#    temp = librosa.effects.pitch_shift(y=temp, sr=sr, n_steps=d[2]/d[3] * 12)
#  listShifted_vocal.extend(temp)


# Audio 제외 음악 파일 output 필요
import soundfile

def get_auto_ok_instance(request):
    state = request.session.get('auto_ok')
    if state is None:
        auto_ok = AutoOk()
        request.session['auto_ok'] = auto_ok.to_dict()
    else:
        auto_ok = AutoOk(state)
    return auto_ok

def save_auto_ok_instance(request, auto_ok):
    request.session['auto_ok'] = auto_ok.to_dict()