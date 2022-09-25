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



#短時間フーリエ変換

stft_result = librosa.stft(wav)
abs_result = np.abs(stft_result)
power_spec = librosa.amplitude_to_db(abs_result, ref=np.max)

plt.figure(figsize=(25,5))
librosa.display.specshow(power_spec, y_axis='log', x_axis='time', sr = sr)
plt.title('Power Spectrogram')
plt.colorbar(format='%+2.0f dB')

plt.tight_layout()





plt.show()