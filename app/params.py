from datetime import datetime
from pathlib import Path


print('----------------------------start params')


#モデル設計におけるパラメータ
INPUT_SIZE = 7
HIDDEN1_SIZE = 2048
HIDDEN2_SIZE = 1024
HIDDEN3_SIZE = 512
HIDDEN4_SIZE = 256
HIDDEN5_SIZE = 128
HIDDEN6_SIZE = 64
HIDDEN7_SIZE = 32
HIDDEN8_SIZE = 8
HIDDEN9_SIZE = 4

OUTPUT_SIZE = 1

EPOCHS = 500
VALIDATION_SPLIT = 0.2 #訓練：テスト=8:2

#印象要素読み込み
imps = '0lig 1cla 2uph 3pas 4sad 5emo 6qui 7fea '
imps = imps.split()  #目的変数y：印象要素(正解データ)

def imp_num(i):

    #グローバル宣言
    global imp, SEED, LEARNING_RATE, DECAY, PATIENCE, DROPOUT

    #0lig
    if i==0:
        imp = imps[i]
        SEED = 6
        LEARNING_RATE = 0.0016
        DECAY = 0.1
        PATIENCE = 16
        DROPOUT = 0.5

        return imp, SEED, LEARNING_RATE, DECAY, PATIENCE, DROPOUT

    #1cla
    elif i==1:
        imp = imps[i]
        SEED = 3
        LEARNING_RATE = 0.001
        DECAY = 0.01
        PATIENCE = 17
        DROPOUT = 0.5
        return imp, SEED, LEARNING_RATE, DECAY, PATIENCE, DROPOUT

    #2uph
    elif i==2:
        imp = imps[i]
        SEED = 1
        LEARNING_RATE = 0.00015
        DECAY = 0.0
        PATIENCE = 10
        DROPOUT = 0.8
        return imp, SEED, LEARNING_RATE, DECAY, PATIENCE, DROPOUT

    #4sad
    elif i==4:
        imp = imps[i]
        SEED = 1
        LEARNING_RATE = 0.0008
        DECAY = 0.1
        PATIENCE = 19
        DROPOUT = 0.6
        return imp, SEED, LEARNING_RATE, DECAY, PATIENCE, DROPOUT

    #6qui
    elif i==6:
        imp = imps[i]
        SEED = 1
        LEARNING_RATE = 0.001
        DECAY = 0.0
        PATIENCE = 20
        DROPOUT = 0.5
        return imp, SEED, LEARNING_RATE, DECAY, PATIENCE, DROPOUT

i = 4  #i(0:8)を変えて複数回利用
imp_num(i)


LOG_DIR = Path('logs/fit') / datetime.now().strftime("%Y%m%d-%H%M%S")
MODEL_FILE_PATH = Path('model.h5')

print('------------------------------end')