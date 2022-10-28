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
newmp3 = sorted(gl.glob('../dataU/*.mp3'), key=lambda f: os.stat(f).st_mtime, reverse=True)
user_music = newmp3[0].replace('../dataU\\', '')
    
# print(user_music)