import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



print('----------------------------raderchart start')

def RaderChart(impsdf):
    # impsdf = create_Udf(i, csvpath)
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()


    # プロットする角度を生成
    angles0 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    angles1 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    angles2 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    angles3 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    angles4 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    angles5 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    angles6 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    angles7 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)

    # 多角形を閉じるためにデータの最後に最初の値を追加
    radar_values0 = np.concatenate(([impsdf.iloc[0, 1:6], [impsdf.iloc[0,1]]]))
    radar_values1 = np.concatenate(([impsdf.iloc[1, 1:6], [impsdf.iloc[1,1]]]))
    radar_values2 = np.concatenate(([impsdf.iloc[2, 1:6], [impsdf.iloc[2,1]]]))
    radar_values3 = np.concatenate(([impsdf.iloc[3, 1:6], [impsdf.iloc[3,1]]]))
    radar_values4 = np.concatenate(([impsdf.iloc[4, 1:6], [impsdf.iloc[4,1]]]))
    radar_values5 = np.concatenate(([impsdf.iloc[5, 1:6], [impsdf.iloc[5,1]]]))
    radar_values6 = np.concatenate(([impsdf.iloc[6, 1:6], [impsdf.iloc[6,1]]]))
    radar_values7 = np.concatenate(([impsdf.iloc[7, 1:6], [impsdf.iloc[7,1]]]))

    fig = plt.figure(figsize=[5.5,5], facecolor='#f2f2f2')
    # 極座標でaxを作成
    ax = fig.add_subplot(1, 1, 1, polar=True)
    
    # 余白を設定
    # plt.subplots_adjust(wspace=0.7, hspace=0.3)

    #レーダーチャートの線を引く
    ax.plot(angles0, radar_values0, color=f'{clrli[0]}')
    ax.plot(angles1, radar_values1, color=f'{clrli[1]}')
    ax.plot(angles2, radar_values2, color=f'{clrli[2]}')
    ax.plot(angles3, radar_values3, color=f'{clrli[3]}')
    ax.plot(angles4, radar_values4, color=f'{clrli[4]}')
    ax.plot(angles5, radar_values5, color=f'{clrli[5]}')
    ax.plot(angles6, radar_values6, color=f'{clrli[6]}')
    ax.plot(angles7, radar_values7, color=f'{clrli[7]}')
    #　レーダーチャートの内側を塗りつぶす
    ax.fill(angles0, radar_values0, alpha=0.1, color=f'{clrli[0]}')
    ax.fill(angles1, radar_values1, alpha=0.1, color=f'{clrli[1]}')
    ax.fill(angles2, radar_values2, alpha=0.1, color=f'{clrli[2]}')
    ax.fill(angles3, radar_values3, alpha=0.1, color=f'{clrli[3]}')
    ax.fill(angles4, radar_values4, alpha=0.1, color=f'{clrli[4]}')
    ax.fill(angles5, radar_values5, alpha=0.1, color=f'{clrli[5]}')
    ax.fill(angles6, radar_values6, alpha=0.1, color=f'{clrli[6]}')
    ax.fill(angles7, radar_values7, alpha=0.1, color=f'{clrli[7]}')

    # 項目ラベルの表示
    ax.set_thetagrids(angles0[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax.set_thetagrids(angles1[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax.set_thetagrids(angles2[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax.set_thetagrids(angles3[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax.set_thetagrids(angles4[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax.set_thetagrids(angles5[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax.set_thetagrids(angles6[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax.set_thetagrids(angles7[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)

    #北を始点
    ax.set_theta_zero_location('N')
    #時計回り
    ax.set_theta_direction(-1)

    # 表示範囲指定
    ax.set_rlim(0, 85)

    # 凡例表示
    ax.legend( ['範囲0', '範囲1', '範囲2', '範囲3', '範囲4', '範囲5', '範囲6', '範囲7'], loc=(-0.15, 0.08), prop={"family":"MS Gothic"})

    # タイトル表示
    # ax.set_title('レーダーチャート', pad=20, fontname="MS Gothic")

    # plt.show()

    return fig


def RaderChart0(impsdf):
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()

    angles0 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    radar_values0 = np.concatenate(([impsdf.iloc[0, 1:6], [impsdf.iloc[0,1]]]))
    
    fig = plt.Figure(figsize=[5.5,5], facecolor='#f2f2f2')
    ax00 = fig.add_subplot(111, projection='polar')
    plt.subplots_adjust(wspace=0.7, hspace=0.3)
    ax00.plot(angles0, radar_values0, color=f'{clrli[0]}')
    ax00.fill(angles0, radar_values0, alpha=0.1, color=f'{clrli[0]}')
    
    ax00.set_thetagrids(angles0[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax00.set_theta_zero_location('N')
    ax00.set_theta_direction(-1)
    ax00.set_rlim(0, 85)
    ax00.set_title('範囲0', pad=10, fontname="MS Gothic", fontsize=15)

    return fig

def RaderChart1(impsdf):
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()

    angles1 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    radar_values1 = np.concatenate(([impsdf.iloc[1, 1:6], [impsdf.iloc[1,1]]]))
    
    fig = plt.Figure(figsize=[5.5,5], facecolor='#f2f2f2')
    ax01 = fig.add_subplot(111, projection='polar')
    plt.subplots_adjust(wspace=0.7, hspace=0.3)
    ax01.plot(angles1, radar_values1, color=f'{clrli[1]}')
    ax01.fill(angles1, radar_values1, alpha=0.1, color=f'{clrli[1]}')
    
    ax01.set_thetagrids(angles1[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax01.set_theta_zero_location('N')
    ax01.set_theta_direction(-1)
    ax01.set_rlim(0, 85)
    ax01.set_title('範囲1', pad=10, fontname="MS Gothic", fontsize=15)

    return fig

def RaderChart2(impsdf):
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()

    angles2 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    radar_values2 = np.concatenate(([impsdf.iloc[2, 1:6], [impsdf.iloc[2,1]]]))
    
    fig = plt.Figure(figsize=[5.5,5], facecolor='#f2f2f2')
    ax02 = fig.add_subplot(111, projection='polar')
    plt.subplots_adjust(wspace=0.7, hspace=0.3)
    ax02.plot(angles2, radar_values2, color=f'{clrli[2]}')
    ax02.fill(angles2, radar_values2, alpha=0.1, color=f'{clrli[2]}')

    ax02.set_thetagrids(angles2[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax02.set_theta_zero_location('N')
    ax02.set_theta_direction(-1)
    ax02.set_rlim(0, 85)
    ax02.set_title('範囲2', pad=10, fontname="MS Gothic", fontsize=15)

    return fig

def RaderChart3(impsdf):
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()

    angles3 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    radar_values3 = np.concatenate(([impsdf.iloc[3, 1:6], [impsdf.iloc[3,1]]]))
    
    fig = plt.Figure(figsize=[5.5,5], facecolor='#f2f2f2')
    ax03 = fig.add_subplot(111, projection='polar')
    plt.subplots_adjust(wspace=0.7, hspace=0.3)
    ax03.plot(angles3, radar_values3, color=f'{clrli[3]}')
    ax03.fill(angles3, radar_values3, alpha=0.1, color=f'{clrli[3]}')

    ax03.set_thetagrids(angles3[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax03.set_theta_zero_location('N')
    ax03.set_theta_direction(-1)
    ax03.set_rlim(0, 85)
    ax03.set_title('範囲3', pad=10, fontname="MS Gothic", fontsize=15)

    return fig

def RaderChart4(impsdf):
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()

    angles4 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    radar_values4 = np.concatenate(([impsdf.iloc[4, 1:6], [impsdf.iloc[4,1]]]))
    
    fig = plt.Figure(figsize=[5.5,5], facecolor='#f2f2f2')
    ax10 = fig.add_subplot(111, projection='polar')
    plt.subplots_adjust(wspace=0.7, hspace=0.3)
    ax10.plot(angles4, radar_values4, color=f'{clrli[4]}')
    ax10.fill(angles4, radar_values4, alpha=0.1, color=f'{clrli[4]}')

    ax10.set_thetagrids(angles4[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax10.set_theta_zero_location('N')
    ax10.set_theta_direction(-1)
    ax10.set_rlim(0, 85)
    ax10.set_title('範囲4', pad=10, fontname="MS Gothic", fontsize=15)

    return fig

def RaderChart5(impsdf):
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()

    angles5 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    radar_values5 = np.concatenate(([impsdf.iloc[5, 1:6], [impsdf.iloc[5,1]]]))
    
    fig = plt.Figure(figsize=[5.5,5], facecolor='#f2f2f2')
    ax11 = fig.add_subplot(111, projection='polar')
    plt.subplots_adjust(wspace=0.7, hspace=0.3)
    ax11.plot(angles5, radar_values5, color=f'{clrli[5]}')
    ax11.fill(angles5, radar_values5, alpha=0.1, color=f'{clrli[5]}')

    ax11.set_thetagrids(angles5[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax11.set_theta_zero_location('N')
    ax11.set_theta_direction(-1)
    ax11.set_rlim(0, 85)
    ax11.set_title('範囲5', pad=10, fontname="MS Gothic", fontsize=15)

    return fig

def RaderChart6(impsdf):
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()

    angles6 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    radar_values6 = np.concatenate(([impsdf.iloc[6, 1:6], [impsdf.iloc[6,1]]]))

    fig = plt.Figure(figsize=[5.5,5], facecolor='#f2f2f2')
    ax12 = fig.add_subplot(111, projection='polar')
    plt.subplots_adjust(wspace=0.7, hspace=0.3)
    ax12.plot(angles6, radar_values6, color=f'{clrli[6]}')
    ax12.fill(angles6, radar_values6, alpha=0.1, color=f'{clrli[6]}')

    ax12.set_thetagrids(angles6[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax12.set_theta_zero_location('N')
    ax12.set_theta_direction(-1)
    ax12.set_rlim(0, 85)
    ax12.set_title('範囲6', pad=10, fontname="MS Gothic", fontsize=15)

    return fig

def RaderChart7(impsdf):
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()

    angles7 = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
    radar_values7 = np.concatenate(([impsdf.iloc[7, 1:6], [impsdf.iloc[7,1]]]))

    fig = plt.Figure(figsize=[5.5,5], facecolor='#f2f2f2')
    ax13 = fig.add_subplot(111, projection='polar')
    plt.subplots_adjust(wspace=0.7, hspace=0.3)
    ax13.plot(angles7, radar_values7, color=f'{clrli[7]}')
    ax13.fill(angles7, radar_values7, alpha=0.1, color=f'{clrli[7]}')

    ax13.set_thetagrids(angles7[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=15)
    ax13.set_theta_zero_location('N')
    ax13.set_theta_direction(-1)
    ax13.set_rlim(0, 85)
    ax13.set_title('範囲7', pad=10, fontname="MS Gothic", fontsize=15)

    return fig



#指定impsのデータフレーム作成(仮記述)
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



#確認用
impsdf = create_Udf(16)
# print(impsdf)
# RaderChart(impsdf)




# class SceneManager():
#     def __init__(self, main_widget):
#         self.m_wid = main_widget

#         self.canvas = FigureCanvasTkAgg(RaderChart(impsdf), master=root)
#         self.canvas.draw()
#         self.canvas.get_tk_widget().place(x = 600, y = 100)




# #ウィンドウ実体化
# root = tk.Tk()
# root.geometry('1520x940+0+0')
# root.title('音楽の印象分析ツール')
# root.configure(bg="yellow")

# #SceneManagerの実体作成
# sm = SceneManager(root)

# root.mainloop()


print('----------------------------raderchart end')