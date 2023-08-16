import pickle
import numpy as np
from sklearn import preprocessing


print('----------------------------preprocessing start')


#
#---------------pkl操作

def save_pkl(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

def read_pkl(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


#
#---------------説明変数の正規化

def preprocess_dataset(data_xy):

    #説明変数の正規化
    scaler = preprocessing.StandardScaler()
    dataset = scaler.fit_transform(np.array(data_xy, dtype = float))
    save_pkl(scaler, path='scaler.pkl')

    scaler = read_pkl(path='scaler.pkl')
    dataset = scaler.transform(dataset)
    return dataset
    

print('------------------------------preprocessing end')