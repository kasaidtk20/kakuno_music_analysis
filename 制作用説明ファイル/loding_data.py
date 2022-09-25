import numpy as np
import matplotlib.pyplot as plt
import glob as gl
import librosa
import librosa.display
from pydub import AudioSegment




print("----------------------------------code")


#データ読み込み

file_name = 'data/Vanitas.wav'
wav, sr = librosa.load(file_name, sr=44100)

plt.figure()
plt.figure(figsize=(10, 4))
librosa.display.waveshow(wav, sr)
plt.title("Wave")



#音声トリミング
music = AudioSegment.from_file("data/Vanitas.wav", format="wav")
time = music.duration_seconds
if time > 120:
    music_trim = music[30000:120000]
else:
    music_trim = music[30000: time * 1000]


#BPM算出
y, sr = librosa.load("data/Vanitas.wav", mono=True)
onset_env = librosa.onset.onset_strength(y, sr=sr)
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
plt.title("BPM")




plt.show()