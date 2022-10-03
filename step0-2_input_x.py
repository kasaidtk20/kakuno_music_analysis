import numpy as np
import librosa
import librosa.display
import os
import csv


print('----------------------------start')


#x名
header = 'filename chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate melspectrogram'
header = header.split()  #説明変数X：音響特徴量

#data_x.csvが存在した場合リセットする
is_file = os.path.isfile('data_x.csv')
if is_file == True:
    os.remove('data_x.csv')
else:
    data_x = open('data_x.csv', 'a', newline='')
    with data_x:
        writer = csv.writer(data_x)
        writer.writerow(header)

data_x.close()

#Xの調達
mp3files = os.listdir('./data')
count = 0
for filename_trim in mp3files:
    if '.mp3' in filename_trim:  #取得ファイルをmp3拡張子のみに制限
        musicname = f'./data/{filename_trim}'
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

data_x.close()


print('------------------------------end')