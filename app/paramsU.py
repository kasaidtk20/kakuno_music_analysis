import os
import glob as gl



# user_music_pre = input('曲の名前：')

# if ' ' in user_music_pre:
#     user_music = user_music_pre.replace(' ', '_')
#     if os.path.isfile(f'../dataU/{user_music_pre}.mp3')==True:
#         os.rename(f'../dataU/{user_music_pre}.mp3', f'../dataU/{user_music}.mp3')
# else:
#     user_music = user_music_pre

# # print(user_music)




#更新日時が最新であるファイル名抽出
def WhatNewFile():
    newmp3 = sorted(gl.glob('../dataU/*.mp3'), key=lambda f: os.stat(f).st_mtime, reverse=True)
    user_music_pre = newmp3[0].replace('../dataU\\', '')
    return user_music_pre

#ファイル名のスペースを置換
def NameReplace(user_music_pre):
    if ' ' in user_music_pre:
        user_music = user_music_pre.replace(' ', '_')
        if os.path.isfile(f'../dataU/{user_music_pre}.mp3')==True:
            if os.path.isfile(f'../dataU/{user_music}.mp3')==False:
                os.rename(f'../dataU/{user_music_pre}.mp3', f'../dataU/{user_music}.mp3')
    else:
        user_music = user_music_pre
    return user_music

# print(NameReplace('ハチ  MV「マトリョシカ」HACHI ⧸ MATORYOSHKA [HOz-9FzIDf0]'))


# print(user_music)