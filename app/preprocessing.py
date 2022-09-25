import numpy as np
import pandas as pd
from nptyping import NDArray, Shape, Float, Int
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from utils import save_pkl, read_pkl


print('----------------------------start')

#各種読み込み
imps = '0lig 1cla 2uph 3pas 4sad 5emo 6qui 7fea '
imps = imps.split()  #目的変数y：印象要素(正解データ)
data_xy = pd.read_csv('../data_xy.csv', encoding = 'shift_jis')
i = 0  #i(0:8)を変えて複数回利用
imp = imps[i]
imps.pop(i)

def preprocess_dataset(dataset: data_xy, is_training: bool) -> data_xy:
    if is_training:
        #data_xy.csvの無関係な列削除    
        data_xy = pd.read_csv('../data_xy.csv', encoding = 'shift_jis')
        data_xy = data_xy.drop(['filename'] + imps, axis=1)
    
        #目的変数名を数値に変換
        impi_list = data_xy.iloc[:, -1]
        encoder = preprocessing.LabelEncoder()
        y = encoder.fit_transform(impi_list)

        #説明変数の正規化
        scaler = preprocessing.StandardScaler()
        X = scaler.fit_transform(np.array(data_xy.iloc[:, :-1], dtype = float))
        save_pkl(scaler, path='scaler.pkl')
        return dataset

    scaler = read_pkl(path='scaler.pkl')
    dataset = scaler.transform(dataset)
    return dataset

    #訓練とテストの分割(8:2)
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('------------------------------end')