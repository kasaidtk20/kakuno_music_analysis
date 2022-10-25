import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import pandas as pd
from yt_dlp import YoutubeDL
import webbrowser

from predictU import predictU_main


print('----------------------------background start')



#Ulog.csv読み込み
def read_csv(j):
    i = 8*j
    Ulog = pd.read_csv('../csv/Ulog.csv', encoding = 'shift_jis')
    index_i =   '軽     清     激     哀     安 ' + '\n' + \
                f'{Ulog.iloc[i,1]} '.rjust(6) + f' {Ulog.iloc[i,2]} '.rjust(6) + f' {Ulog.iloc[i,3]} '.rjust(6) + f' {Ulog.iloc[i,4]} '.rjust(6) + f' {Ulog.iloc[i,5]}'.rjust(6) + '\n' + \
                f'{Ulog.iloc[i+1,1]} '.rjust(6) + f' {Ulog.iloc[i+1,2]} '.rjust(6) + f' {Ulog.iloc[i+1,3]} '.rjust(6) + f' {Ulog.iloc[i+1,4]} '.rjust(6) + f' {Ulog.iloc[i+1,5]}'.rjust(6) + '\n' + \
                f'{Ulog.iloc[i+2,1]} '.rjust(6) + f' {Ulog.iloc[i+2,2]} '.rjust(6) + f' {Ulog.iloc[i+2,3]} '.rjust(6) + f' {Ulog.iloc[i+2,4]} '.rjust(6) + f' {Ulog.iloc[i+2,5]}'.rjust(6) + '\n' + \
                f'{Ulog.iloc[i+3,1]} '.rjust(6) + f' {Ulog.iloc[i+3,2]} '.rjust(6) + f' {Ulog.iloc[i+3,3]} '.rjust(6) + f' {Ulog.iloc[i+3,4]} '.rjust(6) + f' {Ulog.iloc[i+3,5]}'.rjust(6) + '\n' + \
                f'{Ulog.iloc[i+4,1]} '.rjust(6) + f' {Ulog.iloc[i+4,2]} '.rjust(6) + f' {Ulog.iloc[i+4,3]} '.rjust(6) + f' {Ulog.iloc[i+4,4]} '.rjust(6) + f' {Ulog.iloc[i+4,5]}'.rjust(6) + '\n' + \
                f'{Ulog.iloc[i+5,1]} '.rjust(6) + f' {Ulog.iloc[i+5,2]} '.rjust(6) + f' {Ulog.iloc[i+5,3]} '.rjust(6) + f' {Ulog.iloc[i+5,4]} '.rjust(6) + f' {Ulog.iloc[i+5,5]}'.rjust(6) + '\n' + \
                f'{Ulog.iloc[i+6,1]} '.rjust(6) + f' {Ulog.iloc[i+6,2]} '.rjust(6) + f' {Ulog.iloc[i+6,3]} '.rjust(6) + f' {Ulog.iloc[i+6,4]} '.rjust(6) + f' {Ulog.iloc[i+6,5]}'.rjust(6) + '\n' + \
                f'{Ulog.iloc[i+7,1]} '.rjust(6) + f' {Ulog.iloc[i+7,2]} '.rjust(6) + f' {Ulog.iloc[i+7,3]} '.rjust(6) + f' {Ulog.iloc[i+7,4]} '.rjust(6) + f' {Ulog.iloc[i+7,5]}'.rjust(6)
    return index_i



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

        YTutl = 'https://www.youtube.com/'
        webbrowser.open(YTutl, new=2, autoraise=True)


        #オブジェクト
        self.headline = tk.Label(text='分析したい曲を選んでください', font=('', '40', 'bold'), foreground='black')
        self.headline.place(x = 200, y = 200)
        self.description = tk.Label(text='外部の検索画面だよ', font=('', '30'), foreground='black')
        self.description.place(x = 650, y = 400)
        self.Uselected = tk.Button(self.m_wid, text = 'この曲にシマス', font=('', '30'), command=self.Uselected)
        self.Uselected.place(x = 730, y = 750)

    #シーン切り替えの際にSEARCH_MUSIC画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.Uselected.destroy()

#-------------------------------------WAIT(仮)とちゅうううううううううううううううううううううううううううううう

class Wait():
    def __init__(self, main_widget):
        self.m_wid = main_widget


        #オブジェクト
        self.headline = tk.Label(text='しばらくお待ちください', font=('', '60', 'bold'), foreground='black')
        self.headline.place(x = 430, y = 490)

        

    #シーン切り替えの際にWAIT画面からボタンを消す
    def finalize(self):
        self.headline.destroy()

#-------------------------------------RESULT(仮)

class Result():
    def __init__(self, main_widget, END):
        self.m_wid = main_widget
        self.end = END

        #オブジェクト
        self.headline = tk.Label(text='結果', font=('', '40', 'bold'), foreground='black')
        self.headline = self.headline.place(x = 200, y = 200)
        self.description = tk.Label(text='結果だよ', font=('', '30'), foreground='black')
        self.description = self.description.place(x = 650, y = 300)

        self.imps = tk.Label(text=f'{read_csv(1)}', font=('', '17'), foreground='black', justify='right')
        self.imps = self.imps.place(x = 300, y = 400)

        self.end = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.end)
        self.end = self.end.place(x = 730, y = 750)

        

    #シーン切り替えの際にRESULT画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.imps.destroy()
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


        #オブジェクト
        self.headline = tk.Label(text='作成情報', font=('', '60', 'bold'), foreground='black')
        self.headline.place(x = 500, y = 240)
        self.description = tk.Label(text='あ\nい\nう\nえ\nお', font=('', '30'), foreground='black', justify='left')
        self.description.place(x = 650, y = 400)
        self.backtitle = tk.Button(self.m_wid, text = 'タイトルへ戻る', font=('', '30'), command=self.backtitle)
        self.backtitle.place(x = 100, y = 100)

    #シーン切り替えの際にHISTORY画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
        self.backtitle.destroy()


print('----------------------------background end')