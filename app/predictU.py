import numpy as np
from keras.api._v2 import keras
import pandas as pd
from rich import print

import params
from preprocessing import preprocess_dataset


print('----------------------------predictU start')


#数値を5刻みで丸める関数
def multiple_of_5(num):
    num_ = np.round(2*num, -1) / 2
    return num_


def predictU_main():

    #csv読み込み
    filename = pd.read_csv('../csv/data_preset_x.csv', usecols = ['filename'], encoding = 'utf-8')
    Upreds = pd.read_csv('../csv/Ulog.csv', encoding = 'utf-8')


    for i in range(8):
        params.imp_num(i)

        #推論モデル
        def predict(dataset):
            model = keras.models.load_model(params.MODEL_FILE_PATH)
            pred = model.predict(dataset).flatten()
            return pred



        test_data = pd.read_csv('../csv/data_preset_x.csv', 
                                    usecols = ['chroma_stft', 'rmse', 'spectral_centroid', 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate', 'melspectrogram'], 
                                    encoding = 'utf-8')

        #pred_label:予測ラベル  pred_tf:予測ラベルの加工  →  Uのpythonファイル内では印象名(params.imp)で書換
        tp = test_data
        lentp = len(tp)
        test_data = preprocess_dataset(test_data, is_training=True)

        #推論の実行
        pred = predict(dataset=test_data)
        
        #予測ラベル
        #四捨五入
        pred = np.round(pred, 0)
        # pred = multiple_of_5(pred)
        #データフレーム化
        tp[f'{params.imp}'] = pred

        #予測ラベルの加工
        #定義
        def transform(tp):
            max = pred.max()
            min = pred.min()
            tf = (tp[f'{params.imp}'] - min) / (max - min) * 74 + 13
            return tf
        #実行
        pred_tf = transform(tp)
        #四捨五入
        pred_tf = np.round(pred, 0)
        # pred_tf = multiple_of_5(pred_tf)


        #predかpred_tfを選び、test_dataのデータフレームにいずれかの列を追加
        if params.LABEL==7:  #pred_label
            pass
        else:  #pred_tf
            tp[f'{params.imp}'] = pred_tf


        #ユーザーファイルのpredのみを抽出
        Upred = tp.iloc[16:24, 7]

        #Ulog.csvにfilenameと各predを書き込み
        Upreds['filename'] = filename[16:24].reset_index(drop=True)
        Upreds[f'{params.imp}'] = Upred.reset_index(drop=True)

    Upreds_out = Upreds.head(8)
    Upreds_out.to_csv('../csv/Ulog.csv', encoding = 'utf-8', index=False, mode='a', header=False)


    #確認用
    # print(Upreds_out)


    return Upreds_out


print('------------------------------predictU end')