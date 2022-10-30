import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from background import *





#オブジェクト
class SceneManager():
    def __init__(self, main_widget):
        self.m_wid = main_widget

        #-------------------------------------TITLE→START
        

        #TITLE画面ではじめるボタンが押されたときに呼び出される関数
        def changescene_start():
            self.callbutton.finalize()

            self.callbutton = Howto(self.m_wid, changescene_ok, changescene_back)
            
        def changescene_ok():
            self.callbutton.finalize()

            self.callbutton = SearchMusic(self.m_wid, changescene_Uselected, changescene_back)

        def changescene_Uselected():
            self.callbutton.finalize()
            
            self.callbutton = Wait(self.m_wid, changescene_waitto)
            
        def changescene_waitto():
            self.callbutton.finalize()

            self.canvas = FigureCanvasTkAgg(RaderChart(impsdf), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 600, y = 100)

            self.callbutton = Result(self.m_wid, to_rc0, changescene_end)

        def to_rc0():
            canvas0 = FigureCanvasTkAgg(RaderChart0(impsdf), master=root)
            canvas0.draw()
            canvas0.get_tk_widget().place(x = 600, y = 100)

            self.callbutton = Result(self.m_wid, to_rc0, changescene_end)

        
        def changescene_end():
            self.callbutton.finalize()
            self.canvas0.destroy()

            self.callbutton = Title(self.m_wid, changescene_start, changescene_his, changescene_info)






        #-------------------------------------TITLE→HISTORY


        #TITLE画面で履歴ボタンが押されたときに呼び出される関数
        def changescene_his():
            self.callbutton.finalize()

            self.callbutton = His(self.m_wid, changescene_back)

        def changescene_back():
            self.callbutton.finalize()

            self.callbutton = Title(self.m_wid, changescene_start, changescene_his, changescene_info)


        #-------------------------------------TITLE→INFO

        #TITLE画面で作成情報ボタンが押されたときに呼び出される関数
        def changescene_info():
            self.callbutton.finalize()

            self.callbutton = Info(self.m_wid, changescene_back)


        #ボタンなどを画面に表示する実体
        self.callbutton = Title(self.m_wid, changescene_start, changescene_his, changescene_info)





print('----------------------------main start')

#ウィンドウ実体化
root = tk.Tk()
root.geometry('1520x940+0+0')
root.title('音楽の印象分析ツール')
root.configure(bg="yellow")

#SceneManagerの実体作成
sm = SceneManager(root)

root.mainloop()
    

print('----------------------------main end')