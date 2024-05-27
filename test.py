# # pip install ffmpeg-python
# import ffmpeg
# def convert_wav_to_mp3(wav_file_path, mp3_file_path):
#     try:
#         # ffmpeg를 사용하여 변환
#         ffmpeg.input(wav_file_path).output(mp3_file_path).run(cmd=r"C:\Users\bj\Desktop\ffmpeg\bin")
#         print(f"Successfully converted {wav_file_path} to {mp3_file_path}")
#     except ffmpeg.Error as e:
#         print(f"Error converting file: {e.stderr}")
#         return False
#     return True
#
# # 예시 경로
# wav_file_path = '/media/recording.wav'
# mp3_file_path = '/media/recording.mp3'
# print(wav_file_path)
import os
import subprocess

if os.path.exists(r'C:\Users\bj\Desktop\pbl1\media\output.mp3'):
    os.remove(r'C:\Users\bj\Desktop\pbl1\media\output.mp3')
# FFmpeg 명령 구성
command = [
    'ffmpeg',
    '-i', r'C:\Users\bj\Desktop\pbl1\media\MR_file.wav',  # 입력 파일
    r'C:\Users\bj\Desktop\pbl1\media\output.mp3'            # 출력 파일
]

# subprocess.run을 사용하여 명령 실행
try:
    result = subprocess.run(command, check=True, text=True, capture_output=True)
    print("FFmpeg 명령 성공:", result.stdout)
except subprocess.CalledProcessError as e:
    print("FFmpeg 명령 실패:", e.stderr)