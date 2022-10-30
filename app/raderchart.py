import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


print('----------------------------raderchart start')


def RaderChart(impsdf):
    # impsdf = create_Udf(i)
    clrli = ['crimson', 'sandybrown', 'gold', 'aquamarine', 'skyblue', 'steelblue', 'mediumpurple', 'hotpink']
    labels = '軽快・快活 綺麗・清澄 激しい・動的 哀愁・虚無感 静か・安らぎ '
    labels = labels.split()


    # プロットする角度を生成
    # angles = np.linspace(start=0, stop=2*np.pi, num=len(labels)+1, endpoint=True)
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

    # 極座標でaxを作成
    fig, ax = plt.subplots(2,4, figsize=(15, 7), subplot_kw={'projection': 'polar'})
    # 余白を設定
    plt.subplots_adjust(wspace=0.7, hspace=0.3)

    # レーダーチャートの線を引く
    # ax.plot(angles, radar_values0, color=f'{clrli[0]}')
    # ax.plot(angles, radar_values1, color=f'{clrli[1]}')
    # ax.plot(angles, radar_values2, color=f'{clrli[2]}')
    # ax.plot(angles, radar_values3, color=f'{clrli[3]}')
    # ax.plot(angles, radar_values4, color=f'{clrli[4]}')
    # ax.plot(angles, radar_values5, color=f'{clrli[5]}')
    # ax.plot(angles, radar_values6, color=f'{clrli[6]}')
    # ax.plot(angles, radar_values7, color=f'{clrli[7]}')
    ax[0,0].plot(angles0, radar_values0, color=f'{clrli[0]}')
    ax[0,1].plot(angles1, radar_values1, color=f'{clrli[1]}')
    ax[0,2].plot(angles2, radar_values2, color=f'{clrli[2]}')
    ax[0,3].plot(angles3, radar_values3, color=f'{clrli[3]}')
    ax[1,0].plot(angles4, radar_values4, color=f'{clrli[4]}')
    ax[1,1].plot(angles5, radar_values5, color=f'{clrli[5]}')
    ax[1,2].plot(angles6, radar_values6, color=f'{clrli[6]}')
    ax[1,3].plot(angles7, radar_values7, color=f'{clrli[7]}')
    #　レーダーチャートの内側を塗りつぶす
    # ax.fill(angles, radar_values0, alpha=0.1, color=f'{clrli[0]}')
    # ax.fill(angles, radar_values1, alpha=0.1, color=f'{clrli[1]}')
    # ax.fill(angles, radar_values2, alpha=0.1, color=f'{clrli[2]}')
    # ax.fill(angles, radar_values3, alpha=0.1, color=f'{clrli[3]}')
    # ax.fill(angles, radar_values4, alpha=0.1, color=f'{clrli[4]}')
    # ax.fill(angles, radar_values5, alpha=0.1, color=f'{clrli[5]}')
    # ax.fill(angles, radar_values6, alpha=0.1, color=f'{clrli[6]}')
    # ax.fill(angles, radar_values7, alpha=0.1, color=f'{clrli[7]}')
    ax[0,0].fill(angles0, radar_values0, alpha=0.1, color=f'{clrli[0]}')
    ax[0,1].fill(angles1, radar_values1, alpha=0.1, color=f'{clrli[1]}')
    ax[0,2].fill(angles2, radar_values2, alpha=0.1, color=f'{clrli[2]}')
    ax[0,3].fill(angles3, radar_values3, alpha=0.1, color=f'{clrli[3]}')
    ax[1,0].fill(angles4, radar_values4, alpha=0.1, color=f'{clrli[4]}')
    ax[1,1].fill(angles5, radar_values5, alpha=0.1, color=f'{clrli[5]}')
    ax[1,2].fill(angles6, radar_values6, alpha=0.1, color=f'{clrli[6]}')
    ax[1,3].fill(angles7, radar_values7, alpha=0.1, color=f'{clrli[7]}')

    # 項目ラベルの表示
    # ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    # ax[0,0].set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    # ax[0,1].set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    # ax[0,2].set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    # ax[0,3].set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    # ax[1,0].set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    # ax[1,1].set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    # ax[1,2].set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    # ax[1,3].set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    ax[0,0].set_thetagrids(angles0[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    ax[0,1].set_thetagrids(angles1[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    ax[0,2].set_thetagrids(angles2[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    ax[0,3].set_thetagrids(angles3[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    ax[1,0].set_thetagrids(angles4[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    ax[1,1].set_thetagrids(angles5[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    ax[1,2].set_thetagrids(angles6[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)
    ax[1,3].set_thetagrids(angles7[:-1] * 180 / np.pi, labels, fontname="MS Gothic", fontsize=10)

    #北を始点
    # ax.set_theta_zero_location('N')
    ax[0,0].set_theta_zero_location('N')
    ax[0,1].set_theta_zero_location('N')
    ax[0,2].set_theta_zero_location('N')
    ax[0,3].set_theta_zero_location('N')
    ax[1,0].set_theta_zero_location('N')
    ax[1,1].set_theta_zero_location('N')
    ax[1,2].set_theta_zero_location('N')
    ax[1,3].set_theta_zero_location('N')
    #時計回り
    # ax.set_theta_direction(-1)
    ax[0,0].set_theta_direction(-1)
    ax[0,1].set_theta_direction(-1)
    ax[0,2].set_theta_direction(-1)
    ax[0,3].set_theta_direction(-1)
    ax[1,0].set_theta_direction(-1)
    ax[1,1].set_theta_direction(-1)
    ax[1,2].set_theta_direction(-1)
    ax[1,3].set_theta_direction(-1)

    # 表示範囲指定
    # ax.set_rlim(0, 85)
    ax[0,0].set_rlim(0, 85)
    ax[0,1].set_rlim(0, 85)
    ax[0,2].set_rlim(0, 85)
    ax[0,3].set_rlim(0, 85)
    ax[1,0].set_rlim(0, 85)
    ax[1,1].set_rlim(0, 85)
    ax[1,2].set_rlim(0, 85)
    ax[1,3].set_rlim(0, 85)

    # 凡例表示
    # ax.legend( ['part0', 'part1', 'part2', 'part3', 'part4', 'part5', 'part6', 'part7', ], loc=(-0.3, -0.1) )

    # タイトル表示
    # ax.set_title('レーダーチャート', pad=20, fontname="MS Gothic")
    ax[0,0].set_title('part0', pad=20, fontname="MS Gothic")
    ax[0,1].set_title('part1', pad=20, fontname="MS Gothic")
    ax[0,2].set_title('part2', pad=20, fontname="MS Gothic")
    ax[0,3].set_title('part3', pad=20, fontname="MS Gothic")
    ax[1,0].set_title('part4', pad=20, fontname="MS Gothic")
    ax[1,1].set_title('part5', pad=20, fontname="MS Gothic")
    ax[1,2].set_title('part6', pad=20, fontname="MS Gothic")
    ax[1,3].set_title('part7', pad=20, fontname="MS Gothic")

    plt.show()

    return plt.Figure()


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
# impsdf = create_Udf(40)
# print(impsdf)
# RaderChart(impsdf)


print('----------------------------raderchart end')