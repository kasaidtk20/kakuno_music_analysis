import numpy as np
import matplotlib.pyplot as plt
import glob as gl
import librosa
import librosa.display
import pandas as pd
import os
import csv
from pydub import AudioSegment
from tqdm import tqdm
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense


print('----------------------------start')

#各種読み込み
imps = '0lig 1cla 2uph 3pas 4sad 5emo 6qui 7fea '
imps = imps.split()  #目的変数y：印象要素(正解データ)
header = 'filename chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate melspectrogram'
header = header.split()  #説明変数X：音響特徴量

#data = open('data.csv', 'r', newline='')
data = open('data.csv', 'w', newline='')
with data:
    writer = csv.writer(data)
    writer.writerow(header)

#Xの調達
mp3files = os.listdir('./train_data')
count = 0
for filename_trim in mp3files:
    if '.mp3' in filename_trim:  #取得ファイルをmp3拡張子のみに制限
        musicname = f'./train_data/{filename_trim}'
        y, sr = librosa.load(musicname, mono=True, duration=30)

        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        rmse = librosa.feature.rms(y=y)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, win_length=512, hop_length=512)  #shape:(周波数, フレーム数)？  #hop_length:スペクトログラムの横解像度のハイパーパラメータ
        
        to_append = f'{filename_trim} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)} {np.mean(mel_spec)}'
        to_append = to_append.split()
            
        data_x = open('data_x.csv', 'a', newline='')
        with data_x:
            writer = csv.writer(data_x)
            writer.writerow(to_append)
            
        count += 1
        print(count)  #確認用

    else:
        pass


#Xとyを1つのcsvファイルにまとめる
tr_ans_df = pd.read_csv('data_y.csv', encoding = 'UTF-8')
tr_fea_df = pd.read_csv('data_x.csv', encoding = 'shift_jis')
tr_ans_df = tr_ans_df.set_index('filename')
tr_fea_df = tr_fea_df.set_index('filename')

ans_improw = tr_ans_df[imps]

data_xy = pd.merge(tr_fea_df, ans_improw, left_index=True, right_index=True, how='outer')
data_xy = data_xy.groupby(level=0).first()

data_xy.to_csv('data_xy.csv', encoding = 'shift_jis')


data_x.close()


print('------------------------------end')