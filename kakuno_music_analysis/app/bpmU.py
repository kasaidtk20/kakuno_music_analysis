import numpy as np
import matplotlib.pyplot as plt
import librosa
from scipy.signal import argrelmax

import paramsU
import background


print('----------------------------bpmU start')



#music読み込み
y, sr = librosa.load(f'../dataU/{paramsU.user_music}.mp3')
#テンポとビートの抽出
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
tempo = np.round(tempo, decimals=0)
tempo = np.asarray(tempo, dtype = int)
# print(tempo)


print('----------------------------bpmU end')