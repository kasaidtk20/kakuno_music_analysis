from datetime import datetime
from pathlib import Path


print('----------------------------start')

#モデル設計におけるパラメータ
INPUT_SIZE = 7
HIDDEN1_SIZE = 64
HIDDEN2_SIZE = 64
OUTPUT_SIZE = 1

EPOCHS = 500
VALIDATION_SPLIT = 0.2  #訓練：テスト=8:2

LOG_DIR = Path('logs/fit') / datetime.now().strftime("%Y%m%d-%H%M%S")
MODEL_FILE_PATH = Path('model.h5')

print('------------------------------end')