import numpy as np
from keras.api._v2 import keras
import pandas as pd
from rich import print

import params
from preprocessing import preprocess_dataset


print('----------------------------start')

#推論モデル
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

    #test_label:正解ラベル  pred_label:予測ラベル  pred_tf:予測ラベルの加工
    tp = test_label
    lentp = len(tp)
    test_data, test_label = test_data[:lentp], test_label[:lentp]  # lentp分だけ推論をおこなう
    test_data = preprocess_dataset(test_data, is_training=True)

    #推論
    pred = predict(dataset=test_data)
    
    #予測ラベルの整数表示&dataframe化
    pred = np.round(pred, 0)
    tp['pred_label'] = pred


    #予測ラベルの加工を行う
    def transform(tp):
        max = tp['pred_label'].max()
        min = tp['pred_label'].min()
        tf = (tp['pred_label'] - min) / (max - min) * 74 + 13

        return tf
    pred_tf = transform(tp)


    """
    #predの加工
    def transform(tp):
        tp.assign(pred_tf='NaN')

        for pr in list(range(lentp)):
            max = tp['pred_label'].max()
            min = tp['pred_label'].min()
            tf = (tp.at[pr, 'pred_label'] - min) / (max - min) * 80 + 10
            
            test_pred_diff = abs(tp.at[pr, params.imp] - tp.at[pr, 'pred_label'])
            test_predtf_diff = abs(tp.at[pr, params.imp] - tf)

            if test_pred_diff <=10:
                tp.at[pr, 'pred_tf'] = tp.at[pr, 'pred_label']

            else:
                tp.at[pr, 'pred_tf'] = tf
                if test_predtf_diff > test_pred_diff:
                    tp.at[pr, 'pred_tf'] = tp.at[pr, 'pred_label']
                
        return tp['pred_tf']

    pred_tf = transform(tp)
    """

    #予測ラベルの加工の整数表示&dataframe化
    pred_tf = np.round(pred_tf, 0)
    tp['pred_tf'] = pred_tf


    #評価指標&表示
    mae_la = sum( abs( tp[params.imp] - tp['pred_label'] ) ) / lentp
    mae_tf = sum( abs( tp[params.imp] - tp['pred_tf'] ) ) / lentp
    mae_la = np.round(mae_la, 1)  #平均絶対誤差
    mae_tf = np.round(mae_tf, 1)  #平均絶対誤差
    FINAL_PREDICT = min(mae_la, mae_tf)

    print(f'result:\n {tp}')
    print(f'mae_label: {mae_la} / mae_transform: {mae_tf}\nFINAL_PREDICT: {FINAL_PREDICT}')




    print('------------------------------end')