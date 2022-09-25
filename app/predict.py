import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.api._v2 import keras
import pandas as pd
from rich import print

import params
from preprocessing import preprocess_dataset


print('----------------------------start')

#各種読み込み
imps = '0lig 1cla 2uph 3pas 4sad 5emo 6qui 7fea '
imps = imps.split()  #目的変数y：印象要素(正解データ)
i = 0  #i(0:8)を変えて複数回利用
imp = imps[i]
imps.pop(i)

#推論
def predict(dataset):
    model = keras.models.load_model(params.MODEL_FILE_PATH)
    pred = model.predict(dataset).flatten()
    return pred


if __name__ == '__main__':
    test_data = pd.read_csv('../data_xy.csv', 
                                usecols = ['chroma_stft', 'rmse', 'spectral_centroid', 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate', 'melspectrogram'], 
                                encoding = 'shift_jis')
    test_labels = pd.read_csv('../data_xy.csv', 
                                usecols = [imp], 
                                encoding = 'shift_jis')
    test_data, test_labels = test_data[:5], test_labels[:5]  # 5データ分だけ推論をおこなう
    test_data = preprocess_dataset(dataset=test_data, is_training=False)
    pred = predict(dataset=test_data)
    print(f'prediction: {np.round(pred, 1)}')
    print(f'labels: {test_labels}')




    print('------------------------------end')