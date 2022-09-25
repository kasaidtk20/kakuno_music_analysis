import numpy as np
import matplotlib.pyplot as plt
import librosa
from scipy.signal import argrelmax


print('--------------------------------code')


#music読み込み
y, sr = librosa.load('data/c(’ ’＊c[＿＿].wav')
#テンポとビートの抽出
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
tempo = np.round(tempo, decimals=0)
tempo = np.asarray(tempo, dtype = int)
print(tempo)



# onset検出
onset_env = librosa.onset.onset_strength(y, sr=sr)

#予測テンポの図示
hop_length = 512
ac = librosa.autocorrelate(onset_env, 2 * sr // hop_length)
freqs = librosa.tempo_frequencies(len(ac), sr=sr,hop_length=hop_length)

plt.figure(figsize=(8,4))
plt.xlim(10, 300)
plt.plot(freqs,ac,label='Onset autocorrelation')
plt.axvline(tempo, 0, 1, color='r', alpha=0.75, linestyle='--',
           label='Tempo: {:.2f} BPM'.format(tempo))
plt.grid()
plt.title('Static tempo estimation')
plt.legend(frameon=True)
plt.xlabel('Tempo (BPM)')




#極大値の候補をprint
extremum = argrelmax(ac, order=1)
fr = freqs[extremum]
fr = np.round(fr, decimals=0)
fr = np.asarray(fr, dtype = int)

print(fr)




plt.show()