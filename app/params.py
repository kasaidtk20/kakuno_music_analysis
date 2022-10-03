from datetime import datetime
from pathlib import Path


print('----------------------------start')

#印象要素読み込み
imps = '0lig 1cla 2uph 3pas 4sad 5emo 6qui 7fea '
imps = imps.split()  #目的変数y：印象要素(正解データ)
i = 0  #i(0:8)を変えて複数回利用
imp = imps[i]

#モデル設計におけるパラメータ
INPUT_SIZE = 7
HIDDEN1_SIZE = 2048
HIDDEN2_SIZE = 512
HIDDEN3_SIZE = 128
HIDDEN4_SIZE = 16
HIDDEN5_SIZE = 4
HIDDEN6_SIZE = 64
HIDDEN7_SIZE = 32
HIDDEN8_SIZE = 16
HIDDEN9_SIZE = 4

DROPOUT = 0.5

OUTPUT_SIZE = 1

EPOCHS = 500
VALIDATION_SPLIT = 0.2  #訓練：テスト=8:2
LEARNING_RATE = 0.01

LOG_DIR = Path('logs/fit') / datetime.now().strftime("%Y%m%d-%H%M%S")
MODEL_FILE_PATH = Path('model.h5')

print('------------------------------end')