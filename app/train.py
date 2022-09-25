import tensorflow as tf
import pandas as pd
from keras.api._v2 import keras
from keras.models import Model
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from keras.utils import plot_model
import pydoc_data
import graphviz

import params
from preprocessing import preprocess_dataset
from model import DNNModel


print('----------------------------start')

#各種読み込み
imps = '0lig 1cla 2uph 3pas 4sad 5emo 6qui 7fea '
imps = imps.split()  #目的変数y：印象要素(正解データ)
i = 0  #i(0:8)を変えて複数回利用
imp = imps[i]
imps.pop(i)

def main():
    train_data = pd.read_csv('../data_xy.csv', 
                                usecols = ['chroma_stft', 'rmse', 'spectral_centroid', 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate', 'melspectrogram'], 
                                encoding = 'shift_jis')
    train_labels = pd.read_csv('../data_xy.csv', 
                                usecols = [imp], 
                                encoding = 'shift_jis')
    train_data = preprocess_dataset(dataset=train_data, is_training=True)
    train_labels = preprocess_dataset(dataset=train_labels, is_training=True)

    model: Model = DNNModel().build()

    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mae'])
    model.summary()
    plot_model(model, to_file='model.pdf', show_shapes=True)

    callbacks = [
        EarlyStopping(patience=20),
        ModelCheckpoint(filepath=params.MODEL_FILE_PATH, save_best_only=True),
        TensorBoard(log_dir=params.LOG_DIR)]

    model.fit(
        x=train_data,
        y=train_labels,
        epochs=params.EPOCHS,
        validation_split=params.VALIDATION_SPLIT,
        callbacks=callbacks)
    
if __name__ == '__main__':
    main()


print('------------------------------end')