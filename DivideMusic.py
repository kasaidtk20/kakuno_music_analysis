import numpy as np
import matplotlib.pyplot as plt
import glob as gl
import librosa
import librosa.display
import pandas as pd
import os
import csv
from pydub import AudioSegment
from tqdm import tqdm


print('----------------------------start')



#datadir = 'test_data'
datadir= 'train_data'
fullmp3files = os.listdir(f'./{datadir}/full')





#音声トリミング
for filename in fullmp3files:
    #musicファイルの読み込み
    music_add = f'./{datadir}/full/{filename}'
    music = AudioSegment.from_file(music_add, format='mp3')

    #musicファイルから音声の特定部分を抽出
    onetime = (music.duration_seconds / 8)*1000  #ms
    rand = np.random.randint(1,9)
    music_trim = music[onetime*(rand - 1) : onetime*rand]

    #music_trimファイルを出力
    filename_trim = filename.strip('.mp3') + '_trim.mp3'
    music_trim_add = f'./{datadir}/{filename_trim}'
    music_trim.export(music_trim_add, format='mp3')
    print('new_filename:', filename_trim, '/// rand:', rand)



#filename_trim ファイル名出力
for filename in os.listdir(f'./{datadir}/full'):
    print(filename.strip('.mp3') + '_trim.mp3')


"""

trim実行結果

(出力日時：2022/9/19/8:31)
new_filename: Butter-Fly_trim.mp3 /// rand: ?
new_filename: DAYBREAK FRONTLINE_trim.mp3 /// rand: ?
new_filename: drop of regret_trim.mp3 /// rand: 1
new_filename: Feelin Like_trim.mp3 /// rand: 2
new_filename: ごめんね ごめんね_trim.mp3 /// rand: 5
new_filename: ぼかろころしあむ_trim.mp3 /// rand: 3
new_filename: パンドラボックス_trim.mp3 /// rand: 8
new_filename: ミラーチューン_trim.mp3 /// rand: 5
new_filename: 後の橋上_trim.mp3 /// rand: 2
new_filename: 한강의 밤_trim.mp3 /// rand: 4


(出力日時：2022/9/19/8:33)
new_filename: Addiction_trim.mp3 /// rand: 7
new_filename: ARASHI_trim.mp3 /// rand: 7
new_filename: Beware_trim.mp3 /// rand: 8
new_filename: BLACKPINK_trim.mp3 /// rand: 1
new_filename: BR_trim.mp3 /// rand: 6
new_filename: ELECT_trim.mp3 /// rand: 7
new_filename: Fino A Chiamarmi Eva_trim.mp3 /// rand: 4
new_filename: KING_trim.mp3 /// rand: 1
new_filename: LET IT SHINE_trim.mp3 /// rand: 6
new_filename: Nectar_trim.mp3 /// rand: 1
new_filename: Oh Sorry Ya_trim.mp3 /// rand: 6
new_filename: PLASTIC ISLE_trim.mp3 /// rand: 7
new_filename: risk_trim.mp3 /// rand: 3
new_filename: Rocketeer_trim.mp3 /// rand: 5
new_filename: SQUEEZE_trim.mp3 /// rand: 2
new_filename: Ur-Style_trim.mp3 /// rand: 6
new_filename: WiSH VOYAGE_trim.mp3 /// rand: 3
new_filename: アンジェリカ_trim.mp3 /// rand: 2
new_filename: コネクト_trim.mp3 /// rand: 4
new_filename: コールボーイ_trim.mp3 /// rand: 4
new_filename: ジエンド_trim.mp3 /// rand: 4
new_filename: ドラマ_trim.mp3 /// rand: 6
new_filename: ドラマツルギー_trim.mp3 /// rand: 6
new_filename: プライド革命_trim.mp3 /// rand: 3
new_filename: マイナーロールストーリー_trim.mp3 /// rand: 5
new_filename: リスミー_trim.mp3 /// rand: 4
new_filename: レコード・レド　ルカ_trim.mp3 /// rand: 6
new_filename: 光よ_trim.mp3 /// rand: 2
new_filename: 吉原ラメント_trim.mp3 /// rand: 7
new_filename: 地球最後の告白を_trim.mp3 /// rand: 2
new_filename: 妄想税_trim.mp3 /// rand: 4
new_filename: 愛されルート A or B_trim.mp3 /// rand: 4
new_filename: 残酷な天使のテーゼ_trim.mp3 /// rand: 6
new_filename: 浸透圧_trim.mp3 /// rand: 6
new_filename: 深海20love_trim.mp3 /// rand: 4
new_filename: 異類婚姻譚_trim.mp3 /// rand: 3
new_filename: 百代峠_trim.mp3 /// rand: 2
new_filename: 紅蓮華_trim.mp3 /// rand: 5
new_filename: 純愛ロゴス_trim.mp3 /// rand: 8
new_filename: 結ンテ開イテ羅刹ト骸_trim.mp3 /// rand: 7
new_filename: 送る詩_trim.mp3 /// rand: 8
new_filename: 青空Jumping Heart_trim.mp3 /// rand: 2

(出力日時：2022/9/22/13:25)
new_filename: ARASHI_trim.mp3 /// rand: 1
new_filename: Beware_trim.mp3 /// rand: 4
new_filename: LET_IT_SHINE_trim.mp3 /// rand: 2
new_filename: ドラマツルギー_trim.mp3 /// rand: 6
new_filename: 光よ_trim.mp3 /// rand: 7
new_filename: 吉原ラメント_trim.mp3 /// rand: 8
new_filename: 地球最後の告白を_trim.mp3 /// rand: 6
new_filename: 妄想税_trim.mp3 /// rand: 8
new_filename: 残酷な天使のテーゼ_trim.mp3 /// rand: 8
new_filename: 浸透圧_trim.mp3 /// rand: 3
new_filename: 深海20love_trim.mp3 /// rand: 8
new_filename: 百代峠_trim.mp3 /// rand: 8
new_filename: 紅蓮華_trim.mp3 /// rand: 6
new_filename: 純愛ロゴス_trim.mp3 /// rand: 3
new_filename: 結ンテ開イテ羅刹ト骸_trim.mp3 /// rand: 5
new_filename: 送る詩_trim.mp3 /// rand: 7
new_filename: 青空Jumping_Heart_trim.mp3 /// rand: 8

(出力日時：2022/9/22/16:59)
new_filename: 吉原ラメント_trim.mp3 /// rand: 6
new_filename: 地球最後の告白を_trim.mp3 /// rand: 7
new_filename: 結ンテ開イテ羅刹ト骸_trim.mp3 /// rand: 7
new_filename: 青空Jumping_Heart_trim.mp3 /// rand: 7

"""



print('------------------------------end')
