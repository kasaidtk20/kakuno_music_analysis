import pandas as pd

import paramsU
import DivideMusic_and_InputXU
import bpmU
import predictU

PRED = pd.read_csv('../csv/Ulog.csv', encoding = 'shift_jis')
print(f'user_music: {paramsU.user_music}')
print(f'BPM: {bpmU.tempo}')
print(PRED)