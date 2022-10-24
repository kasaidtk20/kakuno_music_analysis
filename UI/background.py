import tkinter as tk
from tkinter import ttk

import time


print('----------------------------background start')



#-------------------------------------TITLE

class Title():
    def __init__(self, main_widget, START, HISTORY):
        self.m_wid = main_widget
        self.start = START
        self.history = HISTORY
        # self.scenenum = 1

    
        #オブジェクト
        self.title = tk.Label(text='音楽分析ツール', font=('', '60', 'bold'), foreground='black')
        self.title.place(x = 500, y = 240)
        self.buttonSTART = tk.Button(self.m_wid, text = 'はじめる', font=('', '30'), command=self.start)
        self.buttonSTART.place(x = 730, y = 600)
        self.buttonHISTORY = tk.Button(self.m_wid, text = '履歴', font=('', '30'), command=self.history)
        self.buttonHISTORY.place(x = 730, y = 750)

    #シーン切り替えの際にTITLE画面からボタンを消す
    def finalize(self):
        self.title.destroy()
        self.buttonSTART.destroy()
        self.buttonHISTORY.destroy()


#-------------------------------------HOWTO

class Howto():
    def __init__(self, main_widget, OK):
        self.m_wid = main_widget
        self.ok = OK


        #オブジェクト
        self.headline = tk.Label(text='使い方', font=('', '60', 'bold'), foreground='black')
        self.headline.place(x = 500, y = 240)
        self.description = tk.Label(text='あ\nい\nう\nえ\nお', font=('', '30'), foreground='black')
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
        self.headline.place(x = 200, y = 200)
        self.description = tk.Label(text='結果だよ', font=('', '30'), foreground='black')
        self.description.place(x = 650, y = 400)
        self.end = tk.Button(self.m_wid, text = '終了', font=('', '30'), command=self.end)
        self.end.place(x = 730, y = 750)

        

    #シーン切り替えの際にRESULT画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.description.destroy()
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
        self.backtitle = tk.Button(self.m_wid, text = '戻る', font=('', '30'), command=self.backtitle)
        self.backtitle.place(x = 100, y = 100)

    #シーン切り替えの際にHISTORY画面からボタンを消す
    def finalize(self):
        self.headline.destroy()
        self.backtitle.destroy()



print('----------------------------background end')