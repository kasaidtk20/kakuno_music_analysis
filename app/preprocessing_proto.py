import numpy as np
from nptyping import NDArray, Shape, Float, Int
from sklearn.preprocessing import StandardScaler

from utils import save_pkl, read_pkl


Features = NDArray[Shape['Sample, Feature'], Float]

def preprocess_dataset(dataset: Features, is_training: bool) -> Features:
    if is_training:
        sc = StandardScaler()
        dataset = sc.fit_transform(dataset)
        save_pkl(sc, path='scaler.pkl')
        return dataset

    sc = read_pkl(path='scaler.pkl')
    dataset = sc.transform(dataset)
    return dataset