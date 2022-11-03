from pydub import AudioSegment

import numpy as np
import librosa
import librosa.display
import csv
import pandas as pd

# import paramsU


print('----------------------------divide-inputxU start')


#DIVIDE MUSIC
def DivideMusic(path, mp3name):

    #ユーザー指定の元ファイル読み込み
    Umusic = open(path)
    # Umusic = open(f'../dataU/{paramsU.user_music}.mp3')

    #音声トリミング
    for i in range(8):
        #musicファイルの読み込み
        music_add = path
        # music_add = f'../dataU/{paramsU.user_music}.mp3'
        music = AudioSegment.from_file(music_add, format='mp3')

        #musicファイルから音声の特定部分を抽出
        onetime = (music.duration_seconds / 8)*1000  #ms
        music_trim = music[onetime*i : onetime*(i + 1)]

        #music_trimファイルを出力
        filename_trim = mp3name + f'_{i}.mp3'
        # filename_trim = f'{paramsU.user_music}' + f'_{i}.mp3'
        music_trim_add = f'../dataU/Umusic/{filename_trim}'
        music_trim.export(music_trim_add, format='mp3')
        # print('new_filename:', filename_trim, '/// number:', i)

    Umusic.close()

    # #分割したら元ファイルを消す
    # os.remove(f'../dataU/{paramsU.user_music}.mp3')




#INPUTX
def Inputx(mp3name):

    #ユーザー行をリセットする
    prex = pd.read_csv('../csv/data_preset_x.csv', encoding = 'utf-8-sig')
    prex = prex.head(16)
    prex.to_csv('../csv/data_preset_x.csv', encoding = 'utf-8-sig', index=False)

    #Xの調達
    for i in range(8):
        musicname = f'../dataU/Umusic/{mp3name}_{i}.mp3'
        # musicname = f'../dataU/Umusic/{paramsU.user_music}_{i}.mp3'
        Umusic = open(musicname)

        y, sr = librosa.load(musicname, mono=True, duration=30)

        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        rmse = librosa.feature.rms(y=y)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, win_length=512, hop_length=512)  #shape:(周波数, フレーム数)？  #hop_length:スペクトログラムの横解像度のハイパーパラメータ

        to_append = f'{mp3name}_{i} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)} {np.mean(mel_spec)}'
        to_append = to_append.split()

        Umusic.close()

        prex = open('../csv/data_preset_x.csv', 'a', newline='', encoding='utf-8')
        with prex:
            writer = csv.writer(prex)
            writer.writerow(to_append)
        prex.close()

        # #Xを調達したら分割ファイルを消す
        # os.remove(musicname)


print('----------------------------divide-inputxU end')