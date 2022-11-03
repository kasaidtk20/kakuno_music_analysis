from time import sleep
from pydub import AudioSegment
import simpleaudio
import pygame

import subprocess
import os
import signal
import sys


#音声再生
def SoundPlayer(path):
    cmd = ['start', f'{path}']
    subprocess.Popen(cmd, shell=True)
    sleep(5)
    subprocess.call('taskkill /im wmplayer.exe')

# SoundPlayer('user_music.mp3')


pred = [7,  7,  6,  9,  5, 13, 13,  4, 14,  7, 15, 13,  9,  9,  6,  8,  6, 14, 14, 12, 15, 16, 14, 11,]
sort = sorted(set(pred))[-2]

print(set(pred))
print(sorted(set(pred))[1])