import numpy as np
import librosa
import pandas as pd
import subprocess

print('----------------------------UIutils start')


#BPM算出関数 in WAIT
def bpmU(path):
    #music読み込み
    y, sr = librosa.load(path)
    #テンポとビートの抽出
    tempo = librosa.beat.beat_track(y=y, sr=sr)
    tempo = np.round(tempo, decimals=0)
    tempo = np.asarray(tempo, dtype = int)
    return tempo



#ユーザー指定のファイルから取得したimpsが、Ulog.csvの中でどこに書かれてあるかを特定 in RESULT
def getUmusic(mp3name, csvpath):
    Ulog = pd.read_csv(csvpath, encoding = 'utf-8')
    filenamelist = Ulog['filename'].to_list()
    Umusicindex = 0
    for j in range(len(filenamelist)):
        if f'{mp3name}' in filenamelist[j]:
            Umusicindex = j
            break
    return Umusicindex

#RESULT画面でimpsをprint in RESULT
def read_csv(i, csvpath):
    # i = Umusicindex
    Ulog = pd.read_csv(csvpath, encoding = 'utf-8')
    Ulogm = Ulog['filename'].astype(str)
    Ulogm_short = Ulogm.str[:8] + '...' + Ulogm.str[-2:]
    Ulog0 = Ulog['0lig'].astype(str)
    Ulog1 = Ulog['1cla'].astype(str)
    Ulog2 = Ulog['2uph'].astype(str)
    Ulog4 = Ulog['4sad'].astype(str)
    Ulog6 = Ulog['6qui'].astype(str)
    global index_m, index_0, index_1, index_2, index_4, index_6

    index_m =  f'範囲\n  \
                {Ulogm_short.iloc[i]}\n  \
                {Ulogm_short.iloc[i+1]}\n  \
                {Ulogm_short.iloc[i+2]}\n  \
                {Ulogm_short.iloc[i+3]}\n  \
                {Ulogm_short.iloc[i+4]}\n  \
                {Ulogm_short.iloc[i+5]}\n  \
                {Ulogm_short.iloc[i+6]}\n  \
                {Ulogm_short.iloc[i+7]}'
    index_m = index_m.replace(' ', '')

    index_0 =  f'軽\n  \
                {Ulog0.iloc[i]}\n  \
                {Ulog0.iloc[i+1]}\n  \
                {Ulog0.iloc[i+2]}\n  \
                {Ulog0.iloc[i+3]}\n  \
                {Ulog0.iloc[i+4]}\n  \
                {Ulog0.iloc[i+5]}\n  \
                {Ulog0.iloc[i+6]}\n  \
                {Ulog0.iloc[i+7]}'
    index_0 = index_0.replace(' ', '').replace('.0', '')
    
    index_1 =  f'清\n  \
                {Ulog1.iloc[i]}\n  \
                {Ulog1.iloc[i+1]}\n  \
                {Ulog1.iloc[i+2]}\n  \
                {Ulog1.iloc[i+3]}\n  \
                {Ulog1.iloc[i+4]}\n  \
                {Ulog1.iloc[i+5]}\n  \
                {Ulog1.iloc[i+6]}\n  \
                {Ulog1.iloc[i+7]}'
    index_1 = index_1.replace(' ', '').replace('.0', '')

    index_2 =  f'激\n  \
                {Ulog2.iloc[i]}\n  \
                {Ulog2.iloc[i+1]}\n  \
                {Ulog2.iloc[i+2]}\n  \
                {Ulog2.iloc[i+3]}\n  \
                {Ulog2.iloc[i+4]}\n  \
                {Ulog2.iloc[i+5]}\n  \
                {Ulog2.iloc[i+6]}\n  \
                {Ulog2.iloc[i+7]}'
    index_2 = index_2.replace(' ', '').replace('.0', '')

    index_4 =  f'哀\n  \
                {Ulog4.iloc[i]}\n  \
                {Ulog4.iloc[i+1]}\n  \
                {Ulog4.iloc[i+2]}\n  \
                {Ulog4.iloc[i+3]}\n  \
                {Ulog4.iloc[i+4]}\n  \
                {Ulog4.iloc[i+5]}\n  \
                {Ulog4.iloc[i+6]}\n  \
                {Ulog4.iloc[i+7]}'
    index_4 = index_4.replace(' ', '').replace('.0', '')

    index_6 =  f'安\n  \
                {Ulog6.iloc[i]}\n  \
                {Ulog6.iloc[i+1]}\n  \
                {Ulog6.iloc[i+2]}\n  \
                {Ulog6.iloc[i+3]}\n  \
                {Ulog6.iloc[i+4]}\n  \
                {Ulog6.iloc[i+5]}\n  \
                {Ulog6.iloc[i+6]}\n  \
                {Ulog6.iloc[i+7]}'
    index_6 = index_6.replace(' ', '').replace('.0', '')

    return index_m, index_0, index_1, index_2, index_4, index_6

#ユーザー指定ファイルから取得したimpsをデータフレーム化 in RESULT
def create_Udf(i, csvpath):
    # i = Umusicindex
    Ulog = pd.read_csv(csvpath, encoding = 'utf-8')
    Ulogm = Ulog['filename']
    Ulog0 = Ulog['0lig']
    Ulog1 = Ulog['1cla']
    Ulog2 = Ulog['2uph']
    Ulog4 = Ulog['4sad']
    Ulog6 = Ulog['6qui']

    Ulog_values = pd.DataFrame([])
    Ulog_values['filename'] = Ulogm
    Ulog_values['0lig'] = Ulog0
    Ulog_values['1cla'] = Ulog1
    Ulog_values['2uph'] = Ulog2
    Ulog_values['4sad'] = Ulog4
    Ulog_values['6qui'] = Ulog6
    Ulog_values = Ulog_values.iloc[i:i+8]
    Ulog_values = Ulog_values.reset_index(drop=True)

    return Ulog_values



#tkinterのウィンドウを最前面or最背面 in SoundPlayer, main.py
def window(root, TF):
    root.attributes("-topmost", TF)

#音声再生 in main.py
def SoundPlayer(root, path):
    cmd = ['start', f'{path}']
    subprocess.Popen(cmd, shell=True)
    # root.lift()
    window(root, True)

#音声終了 in main.py
def SoundKiller():
    subprocess.call('taskkill /im wmplayer.exe')



#変数pathの値を返すだけ in main.py？
def path_return(path):
    return path

#データフレームimpsdf_trueの値を返すだけ in main.py？
def impsdf_true_return(impsdf_true):
    return impsdf_true

#実行結果を変数に保存(未)
def save(mp3name, path, tempo, Umusicindex):
    global mp3name_save, path_save, tempo_save, Umusicindex_save
    mp3name_save = mp3name
    path_save = path
    tempo_save = tempo
    Umusicindex_save = Umusicindex

    return mp3name_save, path_save, tempo_save, Umusicindex_save





print('----------------------------UIutils end')