from time import sleep
# import requests
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from __future__ import unicode_literals
from yt_dlp import YoutubeDL, DownloadError

class Web():


    def __init__(self):

        youtube_url = "https://www.youtube.com/"

        self.start(youtube_url)



    def start(self, url=None, disp = False):

        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
        #待機時間
        # sleep(1)
        if url != None:
            self.browser.get(url)


    def quit(self):
        self.cur_url = self.browser.current_url
        self.browser.quit()

    def download(self):
        
        ydl_opts = {'format': 'best'}

        with YoutubeDL(ydl_opts) as ydl:
            
            try:
                ydl.cache.remove()
                result = ydl.download([self.cur_url])
                print("resullllt::", result)
            except DownloadError as error:
                pass

    def test_url(self):
        self.cur_url = "https://www.youtube.com/watch?v=cm-l2h6GB8Q"
