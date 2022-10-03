import tensorflow as tf
import pandas as pd
import numpy as np
import random
from keras.optimizers import RMSprop
from keras.models import Model, Sequential
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from keras.utils import plot_model
from sklearn.linear_model import LassoCV

import params
from preprocessing import preprocess_dataset
from model import DNNModel


print('----------------------------start')


#シード値固定
SEED = 6
tf.random.set_seed(SEED)
random.seed(SEED)
np.random.seed(SEED)

#読み込み
train_data = pd.read_csv('../data_xy_train.csv', 
                            usecols = ['chroma_stft', 'rmse', 'spectral_centroid', 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate', 'melspectrogram'], 
                            encoding = 'shift_jis')
train_label = pd.read_csv('../data_xy_train.csv', 
                            usecols = [params.imp], 
                            encoding = 'shift_jis')
train_data = preprocess_dataset(train_data, is_training=True)

#RMSprop
rmsprop = RMSprop(lr=0.002, rho=0.9, epsilon=None, decay=0.0)

#学習5
def main():

    model: Model = DNNModel().build()

    model.compile(
        optimizer=rmsprop,
        loss='mse',
        metrics=['mae'])
    model.summary()
    plot_model(model, to_file='model.pdf', show_shapes=True)

    callbacks = [
        EarlyStopping(patience=15),
        ModelCheckpoint(filepath=params.MODEL_FILE_PATH, save_best_only=True),
        TensorBoard(log_dir=params.LOG_DIR)]

    model.fit(
        x=train_data,
        y=train_label,
        epochs=params.EPOCHS,
        verbose=1,
        validation_split=params.VALIDATION_SPLIT,
        callbacks=callbacks,
        initial_epoch=0)
    

if __name__ == '__main__':
    main()



print('------------------------------end')