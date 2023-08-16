import os
import ffmpeg
import glob

class mp4_mp3():

    def all(self, path = ''):
        self.search_mp4()
        self.change_mp4(path)
        self.remove()


    def search_mp4(self):

        mp4 = "*.mp4"
        mp4_name = glob.glob(mp4)
        self.mp4_name = mp4_name[0][:-4]

    def change_mp4(self, path=''):

        # 入力 
        stream = ffmpeg.input(self.mp4_name +".mp4")
        self.name = NameReplace(self.mp4_name)

        # 出力 
        if path == '':
            
            stream = ffmpeg.output(stream, self.name +".mp3")
            self.path_name =  self.name +".mp3"
        else:
            stream = ffmpeg.output(stream, path+"/"+self.name +".mp3")
            self.path_name =  path+"/"+self.name +".mp3"
            
        
        # 実行 
        ffmpeg.run(stream, overwrite_output=True)

    def remove(self):
        mp4_list = glob.glob("*.mp4")
        for mp4 in mp4_list:
            os.remove(mp4)

    
def NameReplace(user_music_pre):
    if ' ' or '　' or '/' or '^' in user_music_pre:
        user_music = user_music_pre.replace(' ', '_').replace('　', '__').replace('/', '_').replace('^', '')
        if os.path.isfile(f'../dataU/{user_music_pre}.mp3')==True:
            if os.path.isfile(f'../dataU/{user_music}.mp3')==False:
                os.rename(f'../dataU/{user_music_pre}.mp3', f'../dataU/{user_music}.mp3')
    else:
        user_music = user_music_pre
    return user_music