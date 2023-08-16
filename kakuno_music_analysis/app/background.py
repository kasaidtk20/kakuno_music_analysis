import tkinter as tk
import pandas as pd
import librosa
import numpy as np
from PIL import Image, ImageTk
import subprocess

from musicDL.webcommand import Web
from musicDL.mp4_mp3 import mp4_mp3
from DivideMusic_and_InputXU import DivideMusic, Inputx
from predictU import predictU_main
# from paramsU import NameReplace
from raderchart import *
from UIutils import *



print('----------------------------background start')


######################################
#-------------------------------------TITLE

class Title():
    def __init__(self, main_widget, START, HISTORY, INFO):
        self.m_wid = main_widget
        self.start = START
        self.history = HISTORY
        self.info = INFO

        openvi1 = Image.open('./media/visual1.png').resize((141,151))
        self.imavi1 = ImageTk.PhotoImage(openvi1)
        openvi0 = Image.open('./media/visual0.png').resize((600, 50))
        self.imavi0 = ImageTk.PhotoImage(openvi0)

    
        #オブジェクト中身
        self.title = tk.Label(text='音楽の印象分析ツール', font=('Rounded Mplus 1c Bold', 60, 'bold'), foreground='black')
        self.vi1 = tk.Label(self.m_wid, image=self.imavi1)
        self.vi0 = tk.Label(self.m_wid, image=self.imavi0)
        self.buttonSTART = tk.Button(self.m_wid, text = ' はじめる ', font=('', '30'), command=self.start)
        self.buttonHISTORY = tk.Button(self.m_wid, text = '前の結果', font=('', '30'), command=self.history)
        self.buttonINFO = tk.Button(self.m_wid, text='作成情報', font=('', '30'), command=self.info)

        #オブジェクト配置
        self.title.place(x = 350, y = 240)
        self.vi1.place(x = 675, y = 350)
        self.vi0.place(x = 460, y = 180)
        # self.buttonSTART.place(x = 655, y = 660)
        self.buttonSTART.place(x = 655, y = 560)
        self.buttonHISTORY.place(x = 655, y = 660)
        self.buttonINFO.place(x = 655, y = 760)

    #シーン切り替えの際にTITLE画面からボタンを消す
    def finalize(self):
        self.title.destroy()
        self.vi1.destroy()
        self.vi0.destroy()
        self.buttonSTART.destroy()
        self.buttonHISTORY.destroy()
        self.buttonINFO.destroy()

#-------------------------------------HOWTO

class Howto():
    def __init__(self, main_widget, OK, BACKTITLE):
        self.m_wid = main_widget
        self.ok = OK
        self.backtitle = BACKTITLE


        #オブジェクト中身
        description =   '①このツールは、機械学習を使って、音楽のBPMや、音楽から受ける印象をスコアとして算出してくれるツールです。\n' +  \
                        '\n' +  \
                        '②「OK」ボタンを押したら、YouTubeにアップロードされている曲の中から好きな曲を選んでください。\n' +  \
                        '\n' +  \
                        '③使用をやめるときは、「タイトルに戻る」ボタンを押してタイトル画面に戻してください。'
        note1 = '※ツールは音楽に対して使うことを推奨しますが、基本どんな音声に対しても機能します。\n' +  \
                '\n' +  \
                '※動画の作成に関わらない者からアップロードされた動画(違法アップロード動画)の選択を避けてください。\n'
        self.headline = tk.Label(text='使用について', font=('', '40', 'bold'), foreground='black')
        self.description = tk.Label(text=description, font=('', '25'), foreground='black', justify='left', wraplength=800)
        self.note1 = tk.Label(text=note1, font=('', '15'), foreground='black', justify='left', wraplength=800)
        self.ok = tk.Button(self.m_wid, text = 'OK', font=('', '30'), command=self.ok)
        self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)

        #オブジェクト配置
        self.headline.place(x = 150, y = 150)
        self.description.place(x = 175, y = 300)
        self.note1.place(x = 175, y = 600)
        self.ok.place(x = 730, y = 800)
        self.backtitle.place(x = 50, y = 50)


    #シーン切り替えの際にHOWTO画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.note1.destroy()
        self.ok.destroy()
        self.backtitle.destroy()

#-------------------------------------SEARTCH_MUSIC

class SearchMusic():
    def __init__(self, main_widget, U_SELECTED, BACKTITLE):
        self.m_wid = main_widget
        self.Uselected = U_SELECTED
        self.backtitle = BACKTITLE

        openvi1 = Image.open('./media/visual1.png').resize((269,288)).transpose(Image.ROTATE_180)
        self.imavi1 = ImageTk.PhotoImage(openvi1)
        openvi3 = Image.open('./media/visual3.png').resize((168,121))
        self.imavi3 = ImageTk.PhotoImage(openvi3)


        #オブジェクト中身
        description =   'ウェブページ上側の検索ボックスから、分析したい曲を探してください。そしてかならず動画の再生画面にしてから「この曲にシマス」ボタンを押してください。\n' +  \
                        '※プレイリスト内にある動画は選択しないでください。→タイトルをコピーして上側の検索ボックスから検索し、同じ動画を選んでください。\n' +  \
                        '\n' +  \
                        '※画面が切り替わるまで1～2分程度お待ちください。\n' +  \
                        '※フリーズしても操作せず、足の裏のシワを見てお待ちくだされ。'
        self.vi1 = tk.Label(self.m_wid, image=self.imavi1)
        self.vi3 = tk.Label(self.m_wid, image=self.imavi3)
        self.headline = tk.Label(text='←YouTubeから分析したい曲を選んでください。', font=('', '30', 'bold'), foreground='black', justify='left', wraplength=400)
        self.description = tk.Label(text=description, font=('', '18'), foreground='black', justify='left', wraplength=380)
        self.Uselected = tk.Button(self.m_wid, text = 'この曲にシマス', font=('', '30'), command=self.Uselected)
        # self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)

        #オブジェクト配置
        self.vi1.place(x = 415, y = 350)
        self.vi3.place(x = 270, y = 240)
        self.headline.place(x = 1100, y = 150)
        self.description.place(x = 1100, y = 350)        
        self.Uselected.place(x = 1100, y = 750)
        # self.backtitle.place(x = 50, y = 50)

        #曲選択
        global web
        web = Web()
        

    #シーン切り替えの際にSEARCH_MUSIC画面からボタンなどを消す
    def finalize(self):
        web.quit()
        
        self.vi1.destroy()
        self.vi3.destroy()
        self.headline.destroy()
        self.description.destroy()
        # self.backtitle.destroy()
        self.Uselected.destroy()

#-------------------------------------WAIT

class Wait():
    def __init__(self, main_widget, WAITTO):
        self.m_wid = main_widget
        self.waitto = WAITTO

        openvi1 = Image.open('./media/visual1.png').resize((101,108))
        self.imavi1 = ImageTk.PhotoImage(openvi1)

        #曲DL
        global mp3name, path, tempo
        web.download()
        mp3 = mp4_mp3()
        mp3.all('../dataU')
        #mp3.name=相対パスと拡張子なし、path=相対パスと拡張子込み
        mp3name = mp3.name
        path = mp3.path_name
        print(f'mp3.name: {mp3.name}')
        print(f'mp3name: {mp3name}')
        print(f'path: {path}')

        #テンポ取得
        tempo = bpmU()
        print(f'テンポ取得完了：{tempo}')
        #分割&x取得
        DivideMusic(path, mp3name)
        print('分割完了')
        Inputx(mp3name)
        print('x取得完了')
        #印象分析
        predictU_main()
        print('印象分析完了')

        #結果の実体
        Umusicindex = getUmusic(mp3name, '../csv/Ulog.csv')
        print(f'Umusicindex:{Umusicindex}')
        read_csv(Umusicindex, '../csv/Ulog.csv')
        global impsdf_true
        impsdf_true = create_Udf(Umusicindex, '../csv/Ulog.csv')

        #分析完了
        self.waitto = tk.Button(self.m_wid, text = '結果を見る', font=('', '30'), command=self.waitto)
        self.vi1 = tk.Label(self.m_wid, image=self.imavi1)
        
        self.waitto.place(x = 1000, y = 670)
        self.vi1.place(x = 1060, y = 750)


    #シーン切り替えの際にWAIT画面からボタンを消す
    def finalize(self):
        self.vi1.destroy()
        self.waitto.destroy()

#-------------------------------------RESULT

class Result():
    def __init__(self, main_widget, PLAYF, PLAY0, PLAY1, PLAY2, PLAY3, PLAY4, PLAY5, PLAY6, PLAY7, RCLEFT, RCRIGHT, END):
        self.m_wid = main_widget
        self.end = END
        self.playf = PLAYF
        self.play0 = PLAY0
        self.play1 = PLAY1
        self.play2 = PLAY2
        self.play3 = PLAY3
        self.play4 = PLAY4
        self.play5 = PLAY5
        self.play6 = PLAY6
        self.play7 = PLAY7
        self.rcl = RCLEFT
        self.rcr = RCRIGHT

        clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']


        #オブジェクト中身
        self.headline = tk.Label(text='結果', font=('', '40', 'bold'), foreground='black')
        self.musicname = tk.Label(text=f'🎵タイトル：{mp3name}', font=('', '35'), foreground='black', justify='left', wraplength=650)
        self.bpm = tk.Label(text=f'BPM：{tempo}', font=('', '40'), fg='black', justify='right')
        self.playf = tk.Button(self.m_wid, text = '全再生', font=('', '13', 'bold'), foreground='black', command=self.playf)
        self.play0 = tk.Button(self.m_wid, text = '再生', font=('', '13', 'bold'), foreground=f'{clrli[0]}', command=self.play0)
        self.play1 = tk.Button(self.m_wid, text = '再生', font=('', '13', 'bold'), foreground=f'{clrli[1]}', command=self.play1)
        self.play2 = tk.Button(self.m_wid, text = '再生', font=('', '13', 'bold'), foreground=f'{clrli[2]}', command=self.play2)
        self.play3 = tk.Button(self.m_wid, text = '再生', font=('', '13', 'bold'), foreground=f'{clrli[3]}', command=self.play3)
        self.play4 = tk.Button(self.m_wid, text = '再生', font=('', '13', 'bold'), foreground=f'{clrli[4]}', command=self.play4)
        self.play5 = tk.Button(self.m_wid, text = '再生', font=('', '13', 'bold'), foreground=f'{clrli[5]}', command=self.play5)
        self.play6 = tk.Button(self.m_wid, text = '再生', font=('', '13', 'bold'), foreground=f'{clrli[6]}', command=self.play6)
        self.play7 = tk.Button(self.m_wid, text = '再生', font=('', '13', 'bold'), foreground=f'{clrli[7]}', command=self.play7)
        self.imps_m = tk.Label(text=index_m, font=('', '25'), fg='black', justify='right')
        self.imps_0 = tk.Label(text=index_0, font=('', '25'), fg='black', justify='right')
        self.imps_1 = tk.Label(text=index_1, font=('', '25'), fg='black', justify='right')
        self.imps_2 = tk.Label(text=index_2, font=('', '25'), fg='black', justify='right')
        self.imps_4 = tk.Label(text=index_4, font=('', '25'), fg='black', justify='right')
        self.imps_6 = tk.Label(text=index_6, font=('', '25'), fg='black', justify='right')
        self.rcl = tk.Button(self.m_wid, text = '◀', font=('', '25'), command=self.rcl)
        self.rcr = tk.Button(self.m_wid, text = '▶', font=('', '25'), command=self.rcr)
        self.note1 = tk.Label(text='※音声は8分割されています。音楽から受けた印象は、分割範囲ごとに数値化されています。単位は%\n  各「再生」ボタンを押すと、グラフと音声が対応します。', font=('', '15'), fg='black', justify='left')
        self.note2 = tk.Label(text='↑範囲ごとの結果を見よう！(音声は対応しません。)', font=('', '15'), fg='black', justify='center')
        self.end = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.end)

        #オブジェクト配置
        px, py, pdif= 120, 536, 33
        ix, iy = 510, 500
        rcx, rcy = 1105, 720
        self.headline.place(x = 200, y = 150)
        self.musicname.place(x = 200, y = 250)
        self.bpm.place(x = 200, y = 420)
        self.playf.place(x = px, y = py-pdif)
        self.play0.place(x = px, y = py)
        self.play1.place(x = px, y = py+pdif)
        self.play2.place(x = px, y = py+2*pdif)
        self.play3.place(x = px, y = py+3*pdif)
        self.play4.place(x = px, y = py+4*pdif)
        self.play5.place(x = px, y = py+5*pdif)
        self.play6.place(x = px, y = py+6*pdif)
        self.play7.place(x = px, y = py+7*pdif)
        self.imps_m.place(x = ix-310, y = iy)
        self.imps_0.place(x = ix, y = iy)
        self.imps_1.place(x = ix+60, y = iy)
        self.imps_2.place(x = ix+120, y = iy)
        self.imps_4.place(x = ix+180, y = iy)
        self.imps_6.place(x = ix+240, y = iy)
        self.rcl.place(x = rcx, y = rcy)
        self.rcr.place(x = rcx+50, y = rcy)
        self.note1.place(x = 150, y = 810)
        self.note2.place(x = 1035, y = 790)
        self.end.place(x = 50, y = 50)

        #確認用
        # print(RaderChart(impsdf))

        

    #シーン切り替えの際にRESULT画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.musicname.destroy()
        self.bpm.destroy()
        self.playf.destroy()
        self.play0.destroy()
        self.play1.destroy()
        self.play2.destroy()
        self.play3.destroy()
        self.play4.destroy()
        self.play5.destroy()
        self.play6.destroy()
        self.play7.destroy()
        self.imps_m.destroy()
        self.imps_0.destroy()
        self.imps_1.destroy()
        self.imps_2.destroy()
        self.imps_4.destroy()
        self.imps_6.destroy()
        self.rcl.destroy()
        self.rcr.destroy()
        self.note1.destroy()
        self.note2.destroy()
        self.end.destroy()

#
#-------------------------------------HISTORY(非表示)

class His():
    def __init__(self, main_widget, BACKTITLE):
        self.m_wid = main_widget
        self.backtitle = BACKTITLE


        #オブジェクト中身
        self.headline = tk.Label(text='履歴', font=('', '40', 'bold'), foreground='black')
        self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)

        #オブジェクト配置
        self.headline.place(x = 150, y = 150)
        self.backtitle.place(x = 50, y = 50)


    #シーン切り替えの際にHISTORY画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.backtitle.destroy()

#
#-------------------------------------RESULT_SAVE
# class ResultSave():


#
#-------------------------------------INFO

class Info():
    def __init__(self, main_widget, BACKTITLE):
        self.m_wid = main_widget
        self.backtitle = BACKTITLE


        #オブジェクト中身
        description =   '・このツールに興味を持ってくれてありがとう！！\n' +  \
                        '\n' +  \
                        '・作成者：関西大学システム理工学部電気電子情報工学科1回生 角野真弓\n' +  \
                        '・指導者：関西大学システム理工学部電気電子情報工学科3回生 大家慧士\n' +  \
                        '・制作期間：2022年9月下旬～同年11月上旬\n' +  \
                        '・制作環境：Windows11のPython 3.10.5のtkinterとかmatplotlibとかpandasとか\n' +  \
                        '・音楽の利用に関して守っていること\n' +  \
                        '→参照：文化庁HPより 著作権法について(第38,47-3,47-7,47-8条)\n' +  \
                        '→https://www.bunka.go.jp/seisaku/chosakuken/seidokaisetsu/gaiyo/chosakubutsu_jiyu.html \n' +  \
                        '・使用画像\n' +  \
                        '→https://www.pngitem.com/middle/hxxRRoo_music-notes-half-circle-hd-png-download/ \n' +  \
                        '・使用BGM\n' +  \
                        '→https://www.youtube.com/watch?v=XjxQew29tCc&t=0s'
        self.headline = tk.Label(text='作成情報', font=('', '40', 'bold'), foreground='black')
        self.description = tk.Label(text=description, font=('', '25'), foreground='black', justify='left', wraplength=830)
        self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)

        #オブジェクト配置
        self.headline.place(x = 150, y = 150)
        self.description.place(x = 150, y = 240)
        self.backtitle.place(x = 50, y = 50)

    #シーン切り替えの際にHISTORY画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.backtitle.destroy()



#
#-------------------------------------(def)

#BPM算出関数 in WAIT
def bpmU():
    #music読み込み
    y, sr = librosa.load(path)
    #テンポとビートの抽出
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    tempo = np.round(tempo, decimals=0)
    tempo = np.asarray(tempo, dtype = int)
    return tempo

#ユーザー指定のファイルから取得したimpsが、Ulog.csvの中でどこに書かれてあるかを特定 in RESULT
def getUmusic(mp3name, csvdir='../csv/Ulog.csv'):
    Ulog = pd.read_csv(csvdir, encoding = 'utf-8')
    filenamelist = Ulog['filename'].to_list()
    Umusicindex = 0
    for j in range(len(filenamelist)):
        if f'{mp3name}' in filenamelist[j]:
            Umusicindex = j
            break
    return Umusicindex

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

#RESULT画面でimpsをprint in RESULT
def read_csv(i, csvdir='../csv/Ulog.csv'):
    # i = Umusicindex
    Ulog = pd.read_csv(csvdir, encoding = 'utf-8')
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
def create_Udf(i, csvdir='../csv/Ulog.csv'):
    # i = Umusicindex
    Ulog = pd.read_csv(csvdir, encoding = 'utf-8')
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

#変数pathの値を返すだけ in main.py
def path_return():
    return path

#データフレームimpsdf_trueの値を返すだけ in main.py
def impsdf_true_return():
    return impsdf_true

#実行結果を変数に保存(未)
def save(mp3name, path, tempo, Umusicindex):
    global mp3name_save, path_save, tempo_save, Umusicindex_save
    mp3name_save = mp3name
    path_save = path
    tempo_save = tempo
    Umusicindex_save = Umusicindex

    return mp3name_save, path_save, tempo_save, Umusicindex_save



print('----------------------------background end')