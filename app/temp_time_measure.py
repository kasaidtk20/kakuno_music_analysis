import time
import pandas as pd
# import paramsU
import os
import glob as gl

# # 時間計測開始
# time_sta = time.perf_counter()
# # 処理を書く（5秒停止する）
# time.sleep(5)
# # 時間計測終了
# time_end = time.perf_counter()
# # 経過時間（秒）
# tim = time_end- time_sta


# Ulog = pd.read_csv('../csv/Ulog.csv', encoding = 'shift_jis')

# print(str(Ulog))




# Ulog = pd.read_csv('../csv/Ulog.csv', encoding = 'shift_jis')
# # Ulog0 = Ulog['0lig'].astype(str).str.replace(' ', '')


# filenamelist = Ulog['filename'].to_list()
# for j in range(len(filenamelist)):
#     if f'{paramsU.user_music}' in filenamelist[j]:
#         Umusicindex = j
#         break
# print(filenamelist)
# print(Umusicindex)




new = sorted(gl.glob('../dataU/*.mp3'), key=lambda f: os.stat(f).st_mtime, reverse=True)
newmp3 = new[0].replace('../dataU\\', '')
    
print(newmp3)