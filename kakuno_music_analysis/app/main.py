import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from background import *





#オブジェクト
class SceneManager():
    def __init__(self, main_widget):
        self.m_wid = main_widget
        SoundPlayer(root, './media/BGM.mp3')


        #-------------------------------------TITLE→START
        

        #TITLE画面ではじめるボタンが押されたときに呼び出される関数
        def changescene_start():
            self.callbutton.finalize()

            self.callbutton = Howto(self.m_wid, changescene_ok, changescene_back)
            
        def changescene_ok():
            self.callbutton.finalize()
        
            SoundKiller()
            window(root, False)

            self.callbutton = SearchMusic(self.m_wid, changescene_Uselected, changescene_back)

        def changescene_Uselected():
            self.callbutton.finalize()

            SoundPlayer(root, './media/BGM.mp3')
            window(root, True)
            
            self.callbutton = Wait(self.m_wid, changescene_waitto)
        
        def changescene_waitto():
            self.callbutton.finalize()

            self.canvas = FigureCanvasTkAgg(RaderChart(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, path_return())

            self.path0 = path_return().replace('dataU', 'dataU/Umusic').replace('.mp3', '_0.mp3')
            self.path1 = path_return().replace('dataU', 'dataU/Umusic').replace('.mp3', '_1.mp3')
            self.path2 = path_return().replace('dataU', 'dataU/Umusic').replace('.mp3', '_2.mp3')
            self.path3 = path_return().replace('dataU', 'dataU/Umusic').replace('.mp3', '_3.mp3')
            self.path4 = path_return().replace('dataU', 'dataU/Umusic').replace('.mp3', '_4.mp3')
            self.path5 = path_return().replace('dataU', 'dataU/Umusic').replace('.mp3', '_5.mp3')
            self.path6 = path_return().replace('dataU', 'dataU/Umusic').replace('.mp3', '_6.mp3')
            self.path7 = path_return().replace('dataU', 'dataU/Umusic').replace('.mp3', '_7.mp3')

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc7, rc0, changescene_end)


        #RESULT画面の分割再生ボタン
        def playf():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, path_return())

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc7, rc0, changescene_end)

        def play0():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart0(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, self.path0)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc, rc1, changescene_end)

        def play1():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart1(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, self.path1)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc0, rc2, changescene_end)

        def play2():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart2(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, self.path2)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc1, rc3, changescene_end)

        def play3():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart3(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, self.path3)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc2, rc4, changescene_end)

        def play4():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart4(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, self.path4)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc3, rc5, changescene_end)

        def play5():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart5(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, self.path5)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc4, rc6, changescene_end)

        def play6():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart6(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, self.path6)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc5, rc7, changescene_end)

        def play7():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart7(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)
            SoundPlayer(root, self.path7)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc6, rc, changescene_end)


        #RESULT画面のレーダーチャート切り替えボタン
        def rc():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc7, rc0, changescene_end)

        def rc0():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart0(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc, rc1, changescene_end)

        def rc1():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart1(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc0, rc2, changescene_end)

        def rc2():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart2(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc1, rc3, changescene_end)

        def rc3():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart3(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc2, rc4, changescene_end)

        def rc4():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart4(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc3, rc5, changescene_end)

        def rc5():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart5(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc4, rc6, changescene_end)

        def rc6():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart6(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc5, rc7, changescene_end)

        def rc7():
            self.callbutton.finalize()

            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart7(impsdf_true_return()), master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().place(x = 870, y = 190)

            self.callbutton = Result(self.m_wid, playf, play0, play1, play2, play3, play4, play5, play6, play7, rc6, rc, changescene_end)

        
        def changescene_end():
            self.callbutton.finalize()
            
            self.canvas.get_tk_widget().place_forget()
            self.canvas = FigureCanvasTkAgg(RaderChart(impsdf_true_return()), master=root)  #噛ませ役
            self.canvas.draw()
            self.canvas.get_tk_widget().place_forget()
            SoundPlayer(root, './media/BGM.mp3')
            # SoundKiller()

            self.callbutton = Title(self.m_wid, changescene_start, changescene_waitto, changescene_info)


        #-------------------------------------TITLE→HISTORY

        #TITLE画面で履歴ボタンが押されたときに呼び出される関数(？？？)
        def changescene_his():
            self.callbutton.finalize()

            self.callbutton = His(self.m_wid, changescene_back)

        def changescene_back():
            self.callbutton.finalize()

            self.callbutton = Title(self.m_wid, changescene_start, changescene_waitto, changescene_info)


        #-------------------------------------TITLE→INFO

        #TITLE画面で作成情報ボタンが押されたときに呼び出される関数
        def changescene_info():
            self.callbutton.finalize()

            self.callbutton = Info(self.m_wid, changescene_back)


        #-------------------------------------
        
        #ボタンなどを画面に表示する実体
        self.callbutton = Title(self.m_wid, changescene_start, changescene_waitto, changescene_info)




print('----------------------------main start')

#ウィンドウ実体化
root = tk.Tk()
root.geometry('1520x940+0+0')
root.title('音楽の印象分析ツール')
root.configure(bg="gray94")

#SceneManagerの実体作成
SceneManager(root)

root.protocol('WM_DELETE_WINDOW', lambda:[SoundKiller(), root.destroy()])
root.mainloop()    

print('----------------------------main end')