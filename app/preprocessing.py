import numpy as np
import pandas as pd
from nptyping import NDArray, Shape, Float, Int
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from utils import save_pkl, read_pkl


print('----------------------------preprocessing start')

def preprocess_dataset(data_xy, is_training: bool):
    if is_training:

        #説明変数の正規化
        scaler = preprocessing.StandardScaler()
        dataset = scaler.fit_transform(np.array(data_xy, dtype = float))
        save_pkl(scaler, path='scaler.pkl')
        return dataset

    scaler = read_pkl(path='scaler.pkl')
    dataset = scaler.transform(dataset)
    return dataset

    #訓練とテストの分割(8:2)
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('------------------------------preprocessing end')