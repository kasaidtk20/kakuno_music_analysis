import numpy as np
import matplotlib.pyplot as plt
import glob
import librosa
from scipy.signal import argrelmax
import pickle


print('--------------------------------code start')


#music読み込み
music_files = glob.glob('data/*.wav')
music_files = [x.replace("\\","/") for x in music_files]
print(music_files)
#['data/c(’ ’＊c[＿＿].wav', 'data/dance.wav', 'data/ELECT.wav', 'data/hide and seek.wav', 'data/Sense of Happiness.wav', 'data/Stick Candy.wav', 
# 'data/Vanitas.wav', 'data/ちきゅう大爆発.wav', 'data/と ても痛い痛がりたい.wav', 'data/アイボリー.wav', 'data/インターアウト！！.wav', 'data/インフェルノ.wav', 
# 'data/ジェット・ラグ.wav', 'data/ドーピングダンス.wav', 'data/ラヴラグ.wav', 'data/㐃.wav', 'data/恋人ごっこ.wav', 'data/時の侭に.wav', 'data/洗濯機と君とラヂオ.wav', 
# 'data/深海20love.wav', 'data/純愛ロゴス.wav', 'data/鏡の音.wav', 'data/青い.wav']


tempo_list = ()
#for i in range(len(music_files)):
for i in range(0,1):
    y, sr = librosa.load(music_files[i])  #y=データ、sr=サンプリング周波数
    #テンポとビートの抽出
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    tempo = np.round(tempo, decimals=0)
    tempo = np.array(tempo, dtype = int)
    i += 1
    tempo_list = np.append(tempo_list, tempo)

print(tempo_list)
#[ 99. 123. 129. 123. 144. 117. 112. 161. 144. 129. 185.  92. 161.  96. 144. 129. 103. 136. 161. 136. 117. 136. 172.]



print('----------------------------code fin')




f = open('tempo_list','w')
pickle.dump(tempo_list,f)
f.close