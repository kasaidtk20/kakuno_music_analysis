import pandas as pd
from preprocessing import preprocess_dataset

"""
data_xy = pd.read_csv('../data_xy.csv', encoding = 'shift_jis')

imps = '0lig 1cla 2uph 3pas 4sad 5emo 6qui 7fea '
imps = imps.split()  #目的変数y：印象要素(正解データ)
i = 0  #i(0:8)を変えて複数回利用
imp = imps[i]

train_data = pd.read_csv('../data_xy.csv', 
                                usecols = ['chroma_stft', 'rmse', 'spectral_centroid', 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate', 'melspectrogram'], 
                                encoding = 'shift_jis')
train_labels = pd.read_csv('../data_xy.csv', 
                                usecols = [imp], 
                                encoding = 'shift_jis')
train_data = preprocess_dataset(dataset=train_data, is_training=True)
train_labels = preprocess_dataset(dataset=train_labels, is_training=True)


print(train_data, '\n----------------\n', train_labels)


print(type(data_xy))

"""