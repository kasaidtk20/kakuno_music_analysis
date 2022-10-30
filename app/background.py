import tkinter as tk
import pandas as pd
import librosa
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

from musicDL.webcommand import Web
from musicDL.mp4_mp3 import mp4_mp3
from musicDL.webcommand import Web
from DivideMusic_and_InputXU import DivideMusic
from DivideMusic_and_InputXU import Inputx
from predictU import predictU_main
from paramsU import NameReplace
from raderchart import RaderChart



print('----------------------------background start')


######################################
#-------------------------------------TITLE

class Title():
    def __init__(self, main_widget, START, HISTORY, INFO):
        self.m_wid = main_widget
        self.start = START
        self.history = HISTORY
        self.info = INFO
        openvi1 = Image.open('visual1.png').resize((141,151))
        self.imavi1 = ImageTk.PhotoImage(openvi1)

    
        #オブジェクト中身
        self.title = tk.Label(text='音楽の印象分析ツール', font=('', '60', 'bold'), foreground='black')
        self.vi1 = tk.Label(self.m_wid, image=self.imavi1)
        self.buttonSTART = tk.Button(self.m_wid, text = ' はじめる ', font=('', '30'), command=self.start)
        self.buttonHISTORY = tk.Button(self.m_wid, text = '   履歴   ', font=('', '30'), command=self.history)
        self.buttonINFO = tk.Button(self.m_wid, text='作成情報', font=('', '30'), command=self.info)

        #オブジェクト配置
        self.title.place(x = 350, y = 240)
        self.vi1.place(x = 675, y = 350)
        self.buttonSTART.place(x = 650, y = 560)
        self.buttonHISTORY.place(x = 655, y = 660)
        self.buttonINFO.place(x = 650, y = 760)

    #シーン切り替えの際にTITLE画面からボタンを消す
    def finalize(self):
        self.title.destroy()
        self.vi1.destroy()
        self.buttonSTART.destroy()
        self.buttonHISTORY.destroy()
        self.buttonINFO.destroy()

#-------------------------------------HOWTO

class Howto():
    def __init__(self, main_widget, OK):
        self.m_wid = main_widget
        self.ok = OK


        #オブジェクト中身
        description =   '①YouTubeにアップされている動画から好きな曲を選んでください。そのときに、動画の作成に関わらない者からアップロードされた動画(違法アップロード動画)の選択を避けてください。\n' +  \
                        '\n' +  \
                        '②選択できる曲は、YouTubeに正規アップロードされているものに限ります。\n' +  \
                        '\n' +  \
                        '③ツールは、音楽に対して使うことを推奨しますが、どんな音声に対しても一応の数値を出すことはできます。\n' +  \
                        '\n' +  \
                        '④使用をやめるときは、「タイトルに戻る」ボタンを押してタイトル画面に戻してください。'
        self.headline = tk.Label(text='使い方', font=('', '40', 'bold'), foreground='black')
        self.description = tk.Label(text=description, font=('', '25'), foreground='black', justify='left', wraplength=1200)
        self.ok = tk.Button(self.m_wid, text = 'OK', font=('', '30'), command=self.ok)
        self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)

        #オブジェクト配置
        self.headline.place(x = 150, y = 150)
        self.description.place(x = 150, y = 300)
        self.ok.place(x = 730, y = 800)
        self.backtitle.place(x = 50, y = 50)


    #シーン切り替えの際にHOWTO画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.ok.destroy()
        self.backtitle.destroy()

#-------------------------------------SEARTCH_MUSIC(仮)

class SearchMusic():
    def __init__(self, main_widget, U_SELECTED):
        self.m_wid = main_widget
        self.Uselected = U_SELECTED


        #オブジェクト中身
        self.headline = tk.Label(text='←ウェブから分析したい曲を選んでください', font=('', '30', 'bold'), foreground='black', justify='left', wraplength=400)
        self.description = tk.Label(text='曲が決まったら「この曲にシマス」を押してください\n※画面が切り替わるまで1分程度お待ちください', font=('', '20'), foreground='black', justify='left', wraplength=380)
        self.Uselected = tk.Button(self.m_wid, text = 'この曲にシマス', font=('', '30'), command=self.Uselected)
        self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)

        #オブジェクト配置
        self.headline.place(x = 1100, y = 200)
        self.description.place(x = 1100, y = 600)        
        self.Uselected.place(x = 1100, y = 750)
        self.backtitle.place(x = 50, y = 50)

        #曲選択&DL
        global web
        web = Web()
        

    #シーン切り替えの際にSEARCH_MUSIC画面からボタンなどを消す
    def finalize(self):
        web.quit()

        self.headline.destroy()
        self.description.destroy()
        self.Uselected.destroy()
        self.backtitle.destroy()

#-------------------------------------WAIT(仮)

class Wait():
    def __init__(self, main_widget, WAITTO):
        self.m_wid = main_widget
        self.waitto = WAITTO

        #曲DL
        global mp3name, path, tempo
        web.download()
        mp3 = mp4_mp3()
        mp3.all('../dataU')
        print(mp3.name)
        #mp3name=相対パスと拡張子なし、path=相対パスと拡張子込み
        mp3name = NameReplace(mp3.name)
        path = mp3.path_name
        print(f'mp3name:{mp3name}')

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

        #分析完了
        self.waitto = tk.Button(self.m_wid, text = '結果を見る', font=('', '30'), command=self.waitto)
        self.waitto.place(x = 1000, y = 750)


    #シーン切り替えの際にWAIT画面からボタンを消す
    def finalize(self):
        self.waitto.destroy()

#-------------------------------------RESULT(仮)

class Result():
    def __init__(self, main_widget, END):
        self.m_wid = main_widget
        self.end = END
        Umusicindex = getUmusic()
        read_csv(Umusicindex)
        global impsdf
        impsdf = create_Udf(Umusicindex)

        #オブジェクト中身
        self.headline = tk.Label(text='結果', font=('', '40', 'bold'), foreground='black')
        self.description = tk.Label(text='結果だよ', font=('', '30'), foreground='black')
        self.bpm = tk.Label(text=f'BPM: {tempo}', font=('', '30'), fg='black', justify='right')
        self.imps_m = tk.Label(text=index_m, font=('', '20'), fg='black', justify='right')
        self.imps_0 = tk.Label(text=index_0, font=('', '20'), fg='black', justify='right')
        self.imps_1 = tk.Label(text=index_1, font=('', '20'), fg='black', justify='right')
        self.imps_2 = tk.Label(text=index_2, font=('', '20'), fg='black', justify='right')
        self.imps_4 = tk.Label(text=index_4, font=('', '20'), fg='black', justify='right')
        self.imps_6 = tk.Label(text=index_6, font=('', '20'), fg='black', justify='right')
        self.end = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.end)

        #オブジェクト配置
        ix, iy = 450, 400
        self.headline.place(x = 200, y = 150)
        self.description.place(x = 650, y = 300)
        self.bpm.place(x = 300, y = 300)
        self.imps_m.place(x = ix-250, y = iy)
        self.imps_0.place(x = ix, y = iy)
        self.imps_1.place(x = ix+70, y = iy)
        self.imps_2.place(x = ix+140, y = iy)
        self.imps_4.place(x = ix+210, y = iy)
        self.imps_6.place(x = ix+280, y = iy)
        self.end.place(x = 50, y = 50)

        #確認用
        print(RaderChart(impsdf))

        

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
#-------------------------------------INFO

class Info():
    def __init__(self, main_widget, BACKTITLE):
        self.m_wid = main_widget
        self.backtitle = BACKTITLE


        #オブジェクト中身
        description =   '・音楽の利用に関して守っていること\n' +  \
                        '→参照：文化庁HPより著作権法について(第38,47-3,47-7,47-8条)\n' +  \
                        '→https://www.bunka.go.jp/seisaku/chosakuken/seidokaisetsu/gaiyo/chosakubutsu_jiyu.html \n' +  \
                        '\n' +  \
                        '・YouTube動画から音楽をダウンロードするときの使用ウェブサイト\n' +  \
                        '→y2mate.com \n'
        self.headline = tk.Label(text='備考', font=('', '40', 'bold'), foreground='black')
        self.description = tk.Label(text=description, font=('', '25'), foreground='black', justify='left', wraplength=1250)
        self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)

        #オブジェクト配置
        self.headline.place(x = 150, y = 150)
        self.description.place(x = 150, y = 300)
        self.backtitle.place(x = 50, y = 50)

    #シーン切り替えの際にHISTORY画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.backtitle.destroy()


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
def getUmusic():
    Ulog = pd.read_csv('../csv/Ulog.csv', encoding = 'utf-8')
    filenamelist = Ulog['filename'].to_list()
    Umusicindex = 0
    for j in range(len(filenamelist)):
        if f'{mp3name}' in filenamelist[j]:
            Umusicindex = j
            break
    return Umusicindex

#RESULT画面でimpsをprint in RESULT
def read_csv(i):
    # i = Umusicindex
    Ulog = pd.read_csv('../csv/Ulog.csv', encoding = 'utf-8')
    Ulogm = Ulog['filename'].astype(str)
    Ulogm_short = Ulogm.str[:8] + '...' + Ulogm.str[-2:]
    Ulog0 = Ulog['0lig'].astype(str)
    Ulog1 = Ulog['1cla'].astype(str)
    Ulog2 = Ulog['2uph'].astype(str)
    Ulog4 = Ulog['4sad'].astype(str)
    Ulog6 = Ulog['6qui'].astype(str)
    global index_m, index_0, index_1, index_2, index_4, index_6

    index_m =  f'パート\n  \
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

#ユーザー指定ファイルから取得したimpsをデータフレーム化 in RESULT
def create_Udf(i):
    # i = Umusicindex
    Ulog = pd.read_csv('../csv/Ulog.csv', encoding = 'utf-8')
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

#レーダーチャートをRESULT画面に表示 in main.py
def RaderChart_show():
    return RaderChart(impsdf)


print('----------------------------background end')