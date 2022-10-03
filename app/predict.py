import numpy as np
from keras.api._v2 import keras
import pandas as pd
from rich import print

import params
from model import DNNModel
from sklearn.linear_model import LassoCV
from preprocessing import preprocess_dataset


print('----------------------------start')

#推論
def predict(dataset):
    model = keras.models.load_model(params.MODEL_FILE_PATH)
    pred = model.predict(dataset).flatten()
    return pred


if __name__ == '__main__':
    test_data = pd.read_csv('../data_xy_test.csv', 
                                usecols = ['chroma_stft', 'rmse', 'spectral_centroid', 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate', 'melspectrogram'], 
                                encoding = 'shift_jis')
    test_label = pd.read_csv('../data_xy_test.csv', 
                                usecols = [params.imp], 
                                encoding = 'shift_jis')
    test_data, test_label = test_data[:20], test_label[:20]  # 5データ分だけ推論をおこなう
    test_data = preprocess_dataset(test_data, is_training=True)
    pred = predict(dataset=test_data)


    pred = np.round(pred, 0)
    test_label['pred_label'] = pred
    tl = test_label
    mae = sum( abs( tl[params.imp] - tl['pred_label'] ) ) / len(tl)
    mae = np.round(mae, 1)  #平均絶対誤差

    print(f'result:\n {tl}')
    print(f'mae: {mae} (ideal: about 10)')




    print('------------------------------end')