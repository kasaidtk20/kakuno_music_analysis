import tkinter as tk
from tkinter import ttk

from background import *
from predictU import predictU_main





#オブジェクト
class SceneManager():
    def __init__(self, main_widget):
        self.m_wid = main_widget

        #-------------------------------------TITLE→START
        
        #TITLE画面ではじめるボタンが押されたときに呼び出される関数
        def changescene_start():
            self.callbutton.finalize()

            self.callbutton = Howto(self.m_wid, changescene_ok)
            
        def changescene_ok():
            self.callbutton.finalize()

            self.callbutton = SearchMusic(self.m_wid, changescene_Uselected)

        def changescene_Uselected():  #とちゅううううううううううううううううううううううううううううううううううううううう
            self.callbutton.finalize()
            # time.sleep(3)
            self.callbutton = Wait(self.m_wid)
            
            # time.sleep(3)
            # predictU_main()
            self.callbutton.finalize()
            # time.sleep(3)
            self.callbutton = Result(self.m_wid, changescene_end)

        def changescene_end():
            self.callbutton.finalize()

            self.callbutton = Title(self.m_wid, changescene_start, changescene_his, changescene_info)





        #-------------------------------------TITLE→HISTORY


        #TITLE画面で履歴ボタンが押されたときに呼び出される関数
        def changescene_his():
            self.callbutton.finalize()

            self.callbutton = His(self.m_wid, changescene_end)


        #-------------------------------------TITLE→INFO

        #TITLE画面でツール情報ボタンが押されたときに呼び出される関数
        def changescene_info():
            self.callbutton.finalize()

            self.callbutton = Info(self.m_wid, changescene_end)


        #ボタンなどを画面に表示する実体
        self.callbutton = Title(self.m_wid, changescene_start, changescene_his, changescene_info)





print('----------------------------main start')

#ウィンドウ実体化
root = tk.Tk()
root.geometry('1920x1080+0+0')
root.title('たいとる')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#SceneManagerの実体作成
sm = SceneManager(root)

root.mainloop()


print('----------------------------main end')