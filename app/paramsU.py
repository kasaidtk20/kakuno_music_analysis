import os


user_music_pre = input('曲の名前：')

if ' ' in user_music_pre:
    user_music = user_music_pre.replace(' ', '_')
    if os.path.isfile(f'../dataU/{user_music_pre}.mp3')==True:
        os.rename(f'../dataU/{user_music_pre}.mp3', f'../dataU/{user_music}.mp3')
else:
    user_music = user_music_pre

# print(user_music)