from re import X
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import pandas as pd
from yt_dlp import YoutubeDL
import glob as gl
import os
import librosa
import numpy as np

from musicDL.webcommand import Web
from musicDL.mp4_mp3 import mp4_mp3
from musicDL.webcommand import Web

# global path

print('----------------------------background start')



#Ulog.csv読み込み
def getUmusic():
    global Umusicindex
    Ulog = pd.read_csv('../csv/Ulog.csv', encoding = 'shift_jis')
    filenamelist = Ulog['filename'].to_list()
    for j in range(len(filenamelist)):
        if f'{paramsU.user_music}' in filenamelist[j]:
            Umusicindex = j
            break
        return Umusicindex
    return Umusicindex

def read_csv(i):
    Ulog = pd.read_csv('../csv/Ulog.csv', encoding = 'shift_jis')
    Ulogm = Ulog['filename'].astype(str)
    Ulog0 = Ulog['0lig'].astype(str)
    Ulog1 = Ulog['1cla'].astype(str)
    Ulog2 = Ulog['2uph'].astype(str)
    Ulog4 = Ulog['4sad'].astype(str)
    Ulog6 = Ulog['6qui'].astype(str)
    global index_m, index_0, index_1, index_2, index_4, index_6

    index_m =  f'パート\n  \
                {Ulogm.iloc[i]}\n  \
                {Ulogm.iloc[i+1]}\n  \
                {Ulogm.iloc[i+2]}\n  \
                {Ulogm.iloc[i+3]}\n  \
                {Ulogm.iloc[i+4]}\n  \
                {Ulogm.iloc[i+5]}\n  \
                {Ulogm.iloc[i+6]}\n  \
                {Ulogm.iloc[i+7]}'
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
    index_0 = index_0.replace(' ', '')
    
    index_1 =  f'清\n  \
                {Ulog1.iloc[i]}\n  \
                {Ulog1.iloc[i+1]}\n  \
                {Ulog1.iloc[i+2]}\n  \
                {Ulog1.iloc[i+3]}\n  \
                {Ulog1.iloc[i+4]}\n  \
                {Ulog1.iloc[i+5]}\n  \
                {Ulog1.iloc[i+6]}\n  \
                {Ulog1.iloc[i+7]}'
    index_1 = index_1.replace(' ', '')

    index_2 =  f'激\n  \
                {Ulog2.iloc[i]}\n  \
                {Ulog2.iloc[i+1]}\n  \
                {Ulog2.iloc[i+2]}\n  \
                {Ulog2.iloc[i+3]}\n  \
                {Ulog2.iloc[i+4]}\n  \
                {Ulog2.iloc[i+5]}\n  \
                {Ulog2.iloc[i+6]}\n  \
                {Ulog2.iloc[i+7]}'
    index_2 = index_2.replace(' ', '')

    index_4 =  f'哀\n  \
                {Ulog4.iloc[i]}\n  \
                {Ulog4.iloc[i+1]}\n  \
                {Ulog4.iloc[i+2]}\n  \
                {Ulog4.iloc[i+3]}\n  \
                {Ulog4.iloc[i+4]}\n  \
                {Ulog4.iloc[i+5]}\n  \
                {Ulog4.iloc[i+6]}\n  \
                {Ulog4.iloc[i+7]}'
    index_4 = index_4.replace(' ', '')

    index_6 =  f'安\n  \
                {Ulog6.iloc[i]}\n  \
                {Ulog6.iloc[i+1]}\n  \
                {Ulog6.iloc[i+2]}\n  \
                {Ulog6.iloc[i+3]}\n  \
                {Ulog6.iloc[i+4]}\n  \
                {Ulog6.iloc[i+5]}\n  \
                {Ulog6.iloc[i+6]}\n  \
                {Ulog6.iloc[i+7]}'
    index_6 = index_6.replace(' ', '')

    return index_m, index_0, index_1, index_2, index_4, index_6



########################################
#-------------------------------------TITLE

class Title():
    def __init__(self, main_widget, START, HISTORY, INFO):
        self.m_wid = main_widget
        self.start = START
        self.history = HISTORY
        self.info = INFO
        # self.scenenum = 1

    
        #オブジェクト
        self.title = tk.Label(text='音楽の印象分析ツール', font=('', '60', 'bold'), foreground='black')
        self.title.place(x = 400, y = 240)
        self.buttonSTART = tk.Button(self.m_wid, text = 'はじめる', font=('', '30'), command=self.start)
        self.buttonSTART.place(x = 730, y = 560)
        self.buttonHISTORY = tk.Button(self.m_wid, text = '履歴', font=('', '30'), command=self.history)
        self.buttonHISTORY.place(x = 730, y = 710)
        self.buttonINFO = tk.Button(self.m_wid, text='ツール情報', font=('', '30'), command=self.info)
        self.buttonINFO.place(x = 730, y = 860)

    #シーン切り替えの際にTITLE画面からボタンを消す
    def finalize(self):
        self.title.destroy()
        self.buttonSTART.destroy()
        self.buttonHISTORY.destroy()
        self.buttonINFO.destroy()


#-------------------------------------HOWTO

class Howto():
    def __init__(self, main_widget, OK):
        self.m_wid = main_widget
        self.ok = OK


        #オブジェクト
        self.headline = tk.Label(text='使い方', font=('', '60', 'bold'), foreground='black')
        self.headline.place(x = 500, y = 240)
        self.description = tk.Label(text='あ\nいい\nう\nえええ\nお', font=('', '30'), foreground='black', justify='left')
        self.description.place(x = 650, y = 400)
        self.ok = tk.Button(self.m_wid, text = 'OK', font=('', '30'), command=self.ok)
        self.ok.place(x = 730, y = 750)

    #シーン切り替えの際にHOWTO画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.ok.destroy()

#-------------------------------------SEARTCH_MUSIC(仮)

class SearchMusic():
    def __init__(self, main_widget, U_SELECTED):
        self.m_wid = main_widget
        self.Uselected = U_SELECTED

        

        #オブジェクト中身
        self.headline = tk.Label(text='分析したい曲を選んでください', font=('', '40', 'bold'), foreground='black')
        self.description = tk.Label(text='外部の検索画面だよ', font=('', '30'), foreground='black')
        self.Uselected = tk.Button(self.m_wid, text = 'この曲にシマス', font=('', '30'), command=self.Uselected)

        #オブジェクト配置
        self.headline.place(x = 200, y = 200)
        self.description.place(x = 650, y = 400)        
        self.Uselected.place(x = 730, y = 750)

        #曲DL
        self.web = Web()
        

    #シーン切り替えの際にSEARCH_MUSIC画面からボタンなどを消す
    def finalize(self):
        self.web.quit()
        self.web.download()
        mp3 = mp4_mp3()
        mp3.all('../dataU')
        print(mp3.name)
        global path
        path = mp3.path_name

        self.headline.destroy()
        self.description.destroy()
        self.Uselected.destroy()

#-------------------------------------WAIT(仮)とちゅうううううううううううううううううううううううううううううう

class Wait():
    def __init__(self, main_widget, WAITTO):
        self.m_wid = main_widget
        self.waitto = WAITTO


        #オブジェクト中身
        self.headline = tk.Label(text='しばらくお待ちください', font=('', '60', 'bold'), foreground='black', )
        
        #オブジェクト配置
        self.headline.place(x = 430, y = 490)


        #テンポ情報
        global tempo
        tempo = bpmU()
        print(tempo)

        # self.waitto()


    #シーン切り替えの際にWAIT画面からボタンを消す
    def finalize(self):
        self.headline.destroy()

#-------------------------------------RESULT(仮)

class Result():
    def __init__(self, main_widget, END):
        self.m_wid = main_widget
        self.end = END

        #オブジェクト中身
        self.headline = tk.Label(text='結果', font=('', '40', 'bold'), foreground='black')
        self.description = tk.Label(text='結果だよ', font=('', '30'), foreground='black')
        self.bpm = tk.Label(text=f'BPM: {tempo}', font=('', '30'), fg='black', justify='right')

        ix = 600
        iy = 500
        getUmusic()
        read_csv(Umusicindex)
        self.imps_m = tk.Label(text=index_m, font=('', '20'), fg='black', justify='right')
        self.imps_0 = tk.Label(text=index_0, font=('', '20'), fg='black', justify='right')
        self.imps_1 = tk.Label(text=index_1, font=('', '20'), fg='black', justify='right')
        self.imps_2 = tk.Label(text=index_2, font=('', '20'), fg='black', justify='right')
        self.imps_4 = tk.Label(text=index_4, font=('', '20'), fg='black', justify='right')
        self.imps_6 = tk.Label(text=index_6, font=('', '20'), fg='black', justify='right')

        #オブジェクト配置
        self.headline = self.headline.place(x = 200, y = 200)
        self.description = self.description.place(x = 650, y = 300)
        self.bpm = self.bpm.place(x = 300, y = 300)
        self.imps_m = self.imps_m.place(x = ix-300, y = iy)
        self.imps_0 = self.imps_0.place(x = ix, y = iy)
        self.imps_1 = self.imps_1.place(x = ix+50, y = iy)
        self.imps_2 = self.imps_2.place(x = ix+100, y = iy)
        self.imps_4 = self.imps_4.place(x = ix+150, y = iy)
        self.imps_6 = self.imps_6.place(x = ix+200, y = iy)

        self.end = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.end)
        self.end = self.end.place(x = 730, y = 750)

        

    #シーン切り替えの際にRESULT画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.bpm.destroy()
        self.imps_m.destroy()
        self.imps_0.destroy()
        self.imps_1.destroy()
        self.imps_2.destroy()
        self.imps_4.destroy()
        self.imps_6.destroy()
        self.end.destroy()

#
#-------------------------------------HISTORY

class His():
    def __init__(self, main_widget, BACKTITLE):
        self.m_wid = main_widget
        self.backtitle = BACKTITLE


        #オブジェクト
        self.headline = tk.Label(text='履歴', font=('', '60', 'bold'), foreground='black')
        self.headline.place(x = 500, y = 240)
        self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)
        self.backtitle.place(x = 100, y = 100)

    #シーン切り替えの際にHISTORY画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.backtitle.destroy()

#
#-------------------------------------INFO

class Info():
    def __init__(self, main_widget, BACKTITLE):
        self.m_wid = main_widget
        self.backtitle = BACKTITLE


        #オブジェクト中身
        self.headline = tk.Label(text='作成情報', font=('', '60', 'bold'), foreground='black')
        self.description = tk.Label(text='あ\nい\nう\nえ\nお', font=('', '30'), foreground='black', justify='left')
        self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)

        #オブジェクト配置
        self.headline.place(x = 500, y = 240)
        self.description.place(x = 650, y = 400)
        self.backtitle.place(x = 100, y = 100)

    #シーン切り替えの際にHISTORY画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.backtitle.destroy()

def bpmU():
    #music読み込み
    y, sr = librosa.load(path)
    #テンポとビートの抽出
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    tempo = np.round(tempo, decimals=0)
    tempo = np.asarray(tempo, dtype = int)
    return tempo

print('----------------------------background end')